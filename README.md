# MedSync

<p align="center">
  <strong>Organize a rotina dos seus medicamentos controlando horários, doses e observações. Encontre o endereço de entrega instantaneamente digitando o CEP.</strong>
</p>

<p align="center">
  <strong>Acesse o sistema:</strong> <a href="https://medsync-main.vercel.app/app" target="_blank">medsync-main.vercel.app/app</a>
</p>

---

## Contexto do Projeto

Este projeto foi desenvolvido como a **Etapa Final da disciplina de Bootcamp** do curso de Engenharia de Software. Ele representa a evolução de uma arquitetura estática para um ecossistema completo com Back-end serverless e persistência em banco de dados relacional.

### A Problemática
A adesão correta a tratamentos médicos é um desafio de saúde pública. Pacientes que utilizam múltiplos medicamentos diariamente enfrentam sérios problemas com a falta de constância, resultando em:
- Esquecimento de horários críticos ou omissão de doses.
- Confusão entre dosagens e recomendações específicas de consumo (ex: ingerir antes ou depois das refeições).
- Descentralização de informações logísticas para a retirada ou entrega de remédios.

### A Solução: MedSync
O **MedSync** nasce para solucionar essas frustrações através de um gerenciamento centralizado e inteligente. O sistema atua como um assistente de saúde focado na usabilidade, permitindo que o usuário organize sua agenda de remédios com precisão. Além disso, automatiza processos logísticos integrando serviços de localização de forma transparente para planejar entregas ou retiradas em postos e farmácias.

---

## 🚀 Funcionalidades do Sistema

O MedSync oferece uma experiência fluida dividida nos seguintes recursos:

- **Autenticação Segura:** Criação de contas e login de usuários com senhas criptografadas via hash PBKDF2 e gerenciamento de sessões com tokens assinados.
- **Segregação de Dados:** Agenda de medicamentos individualizada por conta. Cada usuário tem acesso exclusivo aos seus próprios registros.
- **Gerenciamento de Medicamentos:** Cadastro, listagem em tempo real e remoção de agendamentos contendo nome do remédio, horário, dosagem e notas de observação.
- **Logística via CEP:** Integração com a API pública do **ViaCEP** para simular e preencher instantaneamente endereços válidos de entrega ou retirada de medicamentos.

---

## 🛠️ Tecnologias e Infraestrutura

- **Front-end:** HTML5, CSS3 (Responsivo com Grid e Flexbox) e JavaScript Vanilla.
- **Back-end & API:** Python integrado ao modelo de rotas Serverless da **Vercel**.
- **Banco de Dados:** **Supabase** (PostgreSQL).
- **Qualidade de Código:** Análise estática (Linting) estruturada com o **Flake8** seguindo as diretrizes da PEP 8.
- **Testes Automatizados:** Testes lógicos desenvolvida com **Pytest**.

---

## Arquitetura da API (Rotas Serverless)

| Método | Endpoint | Descrição |
| :--- | :--- | :--- |
| `POST` | `/api/auth/register` | Cria uma nova conta de usuário no banco. |
| `POST` | `/api/auth/login` | Autentica um usuário e gera a sessão protegida. |
| `GET` | `/api/auth/me` | Valida o token e confirma a sessão atual do usuário. |
| `GET` | `/api/medications` | Lista todos os medicamentos agendados do usuário logado. |
| `POST` | `/api/medications` | Registra um novo medicamento vinculado ao `user_id`. |
| `DELETE` | `/api/medications?id={id}` | Remove um medicamento específico da conta ativa. |

---

## Configuração do Ambiente e Banco de Dados (Supabase)

Para o correto funcionamento do ecossistema em nuvem, configure as seguintes variáveis de ambiente na sua plataforma de hospedagem (Vercel):

1. **`DATABASE_URL` ou `POSTGRES_URL`**: A string de conexão do Postgres fornecida pelo Supabase. 
   *(Dica: Dê preferência para a URI do **Transaction Pooler** mantendo o parâmetro `?sslmode=require` ao final.)*
2. **`MEDSYNC_SECRET`**: Uma frase longa e secreta utilizada como chave para a assinatura criptográfica das sessões de login.

 **Nota:** As tabelas são geradas dinamicamente pelas APIs na primeira execução. Caso prefira realizar o provisionamento manual, execute o script localizado em `supabase/schema.sql` diretamente no editor SQL do painel do Supabase.

---

## Como Executar o Projeto Localmente

### Pré-requisitos
- Python 3.12 ou superior instalado.
- Gerenciador de pacotes `pip`.

### Instalação e Execução
1. Clone este repositório para a sua máquina.
2. Instale as dependências listadas no projeto:
   ```bash
   pip install -r requirements.txt
3. Execute o programa principal para a interface via terminal:
    ```bash
   python src/main.py

---

## Execução de Testes e Qualidade
Para validar a lógica e a conformidade do código com as regras de qualidade, utilize os comandos:
1. Executar os testes automatizados
   ```bash
   python -m pytest
2. Executar o linter de verificação de estilo (PEP 8)
   ```bash
   python -m flake8

---

## Deploy na Vercel
O projeto está estruturado para o ecossistema Serverless da Vercel através das diretrizes do arquivo vercel.json:
docs/index.html atua como o ponto de entrada da interface web (/).
api/medications.py processa as requisições de persistência no Postgres.
Para atualizar o ambiente de produção, certifique-se de ter a Vercel CLI instalada e execute:
   ```Bash
   vercel --prod
