# MedSync

Deploy: https://medsync-main.vercel.app/app

Este é o projeto para Etapa Final da disciplina BootCamp. A ideia do MedSync é ajudar no controle de remédios, principalmente para quem toma vários medicamentos no dia, previnindo o esquecimento de algum horário e/ou dose.

## Funcionalidades

## O que da para fazer

* Cadastrar um remedio, horario, dose e observacao.
* Ver a lista de remedios cadastrados.
* Remover um remedio da lista na versao web.
* Criar usuario, fazer login e manter medicamentos separados por conta.
* Consultar um endereco pelo CEP usando a API ViaCEP.
* Usar a versao web pelo navegador.

Na versao web hospedada na Vercel, os remedios ficam salvos no banco Postgres
da Supabase, configurado pela variavel `DATABASE_URL` ou `POSTGRES_URL`. O login
usa senhas com hash PBKDF2 e token assinado. Configure tambem `MEDSYNC_SECRET`
para assinar as sessoes. Se o banco ainda nao existir, a tela usa um modo local
do navegador como fallback para demonstracao.

## Autenticacao e banco

Rotas serverless:

* `POST /api/auth/register` cria uma conta.
* `POST /api/auth/login` entra em uma conta existente.
* `GET /api/auth/me` valida a sessao atual.
* `GET /api/medications` lista remedios do usuario logado.
* `POST /api/medications` cria remedio para o usuario logado.
* `DELETE /api/medications?id={id}` remove remedio do usuario logado.

As tabelas `users` e `medications` sao criadas automaticamente quando as APIs
rodam. A tabela de medicamentos usa `user_id`, entao cada usuario ve apenas a
propria agenda.

## Supabase

1. Crie um projeto no Supabase.
2. Va em **Project Settings > Database**.
3. Copie a connection string do Postgres, de preferencia a connection string
   do **Transaction pooler**, e mantenha `?sslmode=require` no final.
4. Na Vercel, crie a variavel `DATABASE_URL` com essa connection string.
5. Crie tambem `MEDSYNC_SECRET` com uma frase longa e secreta.

Exemplo de formato:

`postgresql://postgres.[PROJECT-REF]:[PASSWORD]@aws-0-[REGION].pooler.supabase.com:6543/postgres?sslmode=require`

O arquivo `supabase/schema.sql` tambem pode ser executado no SQL Editor do
Supabase para criar as tabelas manualmente. Mesmo assim, as APIs tambem tentam
criar as tabelas automaticamente se elas ainda nao existirem.

## API usada

Usamos a API pública ViaCEP para buscar endereços a partir de um CEP.

Endpoint:

`https://viacep.com.br/ws/{cep}/json/`

No projeto, essa consulta serve para simular um endereço de entrega ou retirada de medicamento.

## Como rodar no computador

1. Clone ou baixe o repositório.
2. Instale as dependências:

`pip install -r requirements.txt`

3. Rode o programa no terminal:

`python src/main.py`

Tambem há a possibilidade de abrir o arquivo `main.py` no VS Code e clicar em **Run**.

## Testes

Para rodar os testes:

`python -m pytest`

Para rodar o lint:

`python -m ruff check .`

## Deploy na Vercel com banco

O projeto esta preparado para deploy na Vercel:

* `docs/index.html` e a interface web.
* `api/medications.py` e a API serverless que salva medicamentos em Postgres.
* `vercel.json` direciona `/` para a pagina web e `/api/medications` para a API.

Configure o banco Postgres da Supabase e adicione a variavel de ambiente
`DATABASE_URL` no projeto da Vercel. Se o provedor criar `POSTGRES_URL`, o app
tambem aceita esse nome. Adicione tambem `MEDSYNC_SECRET` com uma frase longa e
secreta para assinar os tokens de login.

Depois, faca o deploy:

`vercel --prod`

## Links

Repositório: https://github.com/pxmarco/Etapa-final/
Deploy: https://medsync-main.vercel.app/app

Autores: Heber Macedo, Marco Antonio, Maria Bertin e Thaynara Lima.
