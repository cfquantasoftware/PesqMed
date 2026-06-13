# App PesqMed

Aplicação desktop (Flet + Python) para cadastro e manutenção da base de médicos,
com backend Postgre, usando otimização NVIDIA RAPIDIS. A primeira tela é o menu principal (`menu.py`).

## Estrutura do projeto

```
PesqMed/
├── .github/workflows/ci.yml   # Pipeline CI/CD (lint + testes)
├── .vscode/                   # Configs do VS Code (testes, debug, extensões)
├── assets/                    # Imagens (LogoSMF.jpg, etc.)
├── src/pesqmed/               # Código-fonte (layout src/)
│   ├── config.py              # Configurações e conexão com o banco
│   ├── services/              # Acesso a dados / regras de negócio
│   └── views/menu.py          # Primeira tela (menu principal)
├── tests/                     # Testes (pytest)
├── data/                      # Dados locais (ignorados pelo git)
├── menu.py                    # Ponto de entrada (primeira tela)
├── pyproject.toml             # Metadados, dependências, ruff e pytest
├── requirements.txt           # Dependências de execução
└── requirements-dev.txt       # Dependências de desenvolvimento
```

## Como rodar (desenvolvimento)

```bash
# 1. Criar e ativar ambiente virtual
python -m venv .venv
.venv\Scripts\activate        # Windows (PowerShell/CMD)

# 2. Instalar dependências de desenvolvimento
pip install -r requirements-dev.txt

# 3. Copiar variáveis de ambiente e preencher
copy .env.example .env        # Windows

# 4. Rodar a aplicação (primeira tela)
python menu.py
# ou
flet run menu.py
```

## Qualidade (rodar local antes de commitar)

```bash
ruff check .          # lint
ruff format .         # formatação
pytest -v             # testes
```

## CI/CD

A cada `push` ou `pull request` para `main`/`master`, o GitHub Actions executa
lint (ruff), checagem de formatação e os testes (pytest). Veja
[.github/workflows/ci.yml](.github/workflows/ci.yml).

## Versionamento

- `main` / `master`: código estável.
- Crie um branch por funcionalidade (`feat/lista-medicos`, `fix/...`) e abra PR.
- Segredos (senha do banco) ficam no `.env` (não versionado) — veja `.env.example`.
