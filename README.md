# Task Manager API

![CI](https://github.com/GabrielBorges240/task-manager-api/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.12-blue)
![License](https://img.shields.io/badge/license-MIT-green)

API RESTful para gerenciamento de tarefas, construída com FastAPI, PostgreSQL, Docker e autenticação JWT. O projeto aplica boas práticas de desenvolvimento backend: acesso assíncrono ao banco, migrações, testes automatizados e integração contínua.

**Demo online:** https://task-manager-api-dsle.onrender.com/docs

> O deploy usa o plano gratuito do Render. Se a API estiver inativa, a primeira requisição pode levar cerca de um minuto para responder.

## Tecnologias

- **FastAPI**: framework web assíncrono de alto desempenho
- **PostgreSQL**: banco de dados relacional
- **SQLAlchemy (async)**: ORM com suporte assíncrono
- **Alembic**: migrações de banco de dados
- **JWT**: autenticação stateless
- **Docker e Docker Compose**: containerização do ambiente
- **Pytest**: testes automatizados com relatório de cobertura
- **GitHub Actions**: integração contínua (CI)

## Funcionalidades

- Registro e login de usuários com JWT
- CRUD completo de tarefas
- Filtros por status, prioridade e estado de conclusão
- Paginação das listagens
- Rotas protegidas e isolamento de dados por usuário: cada usuário acessa apenas as próprias tarefas (prevenção de BOLA)
- Testes de integração com relatório de cobertura

## Arquitetura

O código é dividido em camadas para separar responsabilidades:

- `routers/`: recebem as requisições HTTP e devolvem as respostas
- `services/`: regras de negócio
- `repositories/`: acesso ao banco de dados
- `schemas/`: validação de entrada e saída (Pydantic)
- `models/`: modelos do banco (SQLAlchemy)

## Como executar

### Com Docker (recomendado)

```bash
git clone https://github.com/GabrielBorges240/task-manager-api.git
cd task-manager-api

cp .env.example .env
docker compose up -d
docker compose exec api alembic upgrade head
```

Documentação interativa: http://localhost:8000/docs

### Ambiente local

```bash
python -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate

pip install -r requirements.txt
cp .env.example .env
alembic upgrade head
uvicorn app.main:app --reload
```

## Variáveis de ambiente

Copie `.env.example` para `.env` e ajuste os valores. Nunca envie o `.env` para o repositório.

| Variável | Descrição |
|---|---|
| `DATABASE_URL` | URL de conexão com o PostgreSQL |
| `SECRET_KEY` | Chave usada para assinar os tokens JWT |
| `ALGORITHM` | Algoritmo do JWT (ex.: `HS256`) |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Tempo de expiração do token |

## Endpoints

### Autenticação

| Método | Endpoint | Descrição |
|---|---|---|
| POST | `/auth/register` | Cria uma nova conta |
| POST | `/auth/login` | Autentica e retorna o token de acesso |

### Usuários

| Método | Endpoint | Descrição |
|---|---|---|
| GET | `/users/me` | Retorna o perfil do usuário autenticado |
| PATCH | `/users/me` | Atualiza o perfil do usuário autenticado |

### Tarefas

| Método | Endpoint | Descrição |
|---|---|---|
| POST | `/tasks` | Cria uma tarefa |
| GET | `/tasks` | Lista as tarefas do usuário (com filtros e paginação) |
| GET | `/tasks/{id}` | Busca uma tarefa por ID |
| PATCH | `/tasks/{id}` | Atualiza uma tarefa |
| DELETE | `/tasks/{id}` | Exclui uma tarefa |

## Exemplo de uso

```bash
# 1. Registrar
curl -X POST http://localhost:8000/auth/register \
  -H "Content-Type: application/json" \
  -d '{"name": "Gabriel", "email": "gabriel@email.com", "password": "123456"}'

# 2. Fazer login e copiar o access_token
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "gabriel@email.com", "password": "123456"}'

# 3. Criar uma tarefa
curl -X POST http://localhost:8000/tasks \
  -H "Authorization: Bearer SEU_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title": "Estudar FastAPI", "priority": "high"}'

# 4. Listar tarefas pendentes
curl "http://localhost:8000/tasks?status=pending&page=1&limit=20" \
  -H "Authorization: Bearer SEU_TOKEN"
```

## Testes

```bash
pytest tests/ -v --cov=app --cov-report=term-missing
```

## Estrutura do projeto

```
task-manager-api/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── models/
│   ├── schemas/
│   ├── repositories/
│   ├── routers/
│   └── services/
├── tests/
├── alembic/
├── Dockerfile
├── docker-compose.yml
└── .github/workflows/
```

## Próximos passos

- Refresh token e logout
- Rate limiting
- Busca por texto e ordenação nas listagens
- Deploy automatizado (CD)

## Licença

Distribuído sob a licença MIT.

## Autor

**Gabriel Borges**
Desenvolvedor backend em Python, com foco em APIs, arquitetura de software e boas práticas.

[GitHub](https://github.com/GabrielBorges240)
