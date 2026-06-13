"""Configurações centrais do App PesqMed.

Valores sensíveis (senha do banco, etc.) devem vir de variáveis de ambiente
(arquivo .env, NÃO versionado). Veja .env.example.
"""

import os

APP_TITLE = "App PesqMed"
LOGO = "LogoSMF.jpg"  # relativo a assets/

# Conexão com o banco MySQL (sobrescreva via variáveis de ambiente)
DB_HOST = os.getenv("PESQMED_DB_HOST", "localhost")
DB_PORT = int(os.getenv("PESQMED_DB_PORT", "3306"))
DB_NAME = os.getenv("PESQMED_DB_NAME", "smf")
DB_USER = os.getenv("PESQMED_DB_USER", "root")
DB_PASSWORD = os.getenv("PESQMED_DB_PASSWORD", "")
