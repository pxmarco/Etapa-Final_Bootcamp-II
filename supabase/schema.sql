CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS medications (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    name TEXT NOT NULL,
    time TEXT NOT NULL,
    dose TEXT NOT NULL DEFAULT '',
    note TEXT NOT NULL DEFAULT '',
    cep TEXT NOT NULL DEFAULT '',
    logradouro TEXT NOT NULL DEFAULT '',
    cidade TEXT NOT NULL DEFAULT '',
    uf TEXT NOT NULL DEFAULT '',
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS medications_user_id_time_idx
ON medications (user_id, time, created_at);
