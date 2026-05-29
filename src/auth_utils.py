import base64
import binascii
import hashlib
import hmac
import json
import os
import secrets
import time


TOKEN_TTL_SECONDS = 60 * 60 * 24 * 7


def json_response(handler, status, payload):
    body = json.dumps(payload).encode("utf-8")
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json; charset=utf-8")
    handler.send_header("Content-Length", str(len(body)))
    handler.end_headers()
    handler.wfile.write(body)


def read_json(handler):
    length = int(handler.headers.get("Content-Length", "0"))
    if length == 0:
        return {}
    return json.loads(handler.rfile.read(length).decode("utf-8"))


def token_secret():
    secret = os.environ.get("MEDSYNC_SECRET") or os.environ.get("AUTH_SECRET")
    if secret:
        return secret.encode("utf-8")

    database_url = os.environ.get("DATABASE_URL") or os.environ.get("POSTGRES_URL")
    if database_url:
        return hashlib.sha256(database_url.encode("utf-8")).digest()

    return b"medsync-local-development-secret"


def b64_encode(data):
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("ascii")


def b64_decode(value):
    padding = "=" * (-len(value) % 4)
    return base64.urlsafe_b64decode((value + padding).encode("ascii"))


def hash_password(password):
    salt = secrets.token_bytes(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 260000)
    return f"pbkdf2_sha256$260000${b64_encode(salt)}${b64_encode(digest)}"


def verify_password(password, stored_hash):
    try:
        algorithm, iterations, salt, expected = stored_hash.split("$", 3)
        if algorithm != "pbkdf2_sha256":
            return False
        digest = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            b64_decode(salt),
            int(iterations),
        )
        return hmac.compare_digest(b64_encode(digest), expected)
    except (binascii.Error, ValueError, TypeError):
        return False


def create_token(user_id):
    payload = {
        "sub": str(user_id),
        "iat": int(time.time()),
        "exp": int(time.time()) + TOKEN_TTL_SECONDS,
    }
    encoded_payload = b64_encode(json.dumps(payload, separators=(",", ":")).encode("utf-8"))
    signature = hmac.new(token_secret(), encoded_payload.encode("ascii"), hashlib.sha256)
    return f"{encoded_payload}.{b64_encode(signature.digest())}"


def parse_token(token):
    try:
        encoded_payload, signature = token.split(".", 1)
        expected_signature = hmac.new(
            token_secret(),
            encoded_payload.encode("ascii"),
            hashlib.sha256,
        ).digest()
        if not hmac.compare_digest(b64_decode(signature), expected_signature):
            return None

        payload = json.loads(b64_decode(encoded_payload).decode("utf-8"))
        if int(payload.get("exp", 0)) < int(time.time()):
            return None
        return payload
    except (binascii.Error, ValueError, TypeError, json.JSONDecodeError):
        return None


def bearer_token(headers):
    authorization = headers.get("Authorization", "")
    prefix = "Bearer "
    if not authorization.startswith(prefix):
        return ""
    return authorization[len(prefix) :].strip()


def public_user(row):
    return {
        "id": str(row["id"]),
        "name": row["name"],
        "email": row["email"],
    }


def user_initials(name):
    parts = str(name or "").strip().split()
    if not parts:
        return "--"
    return "".join(part[0] for part in parts[:2]).upper()
