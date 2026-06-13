"""Ponto de entrada do App PesqMed — primeira tela (menu principal).

Execute com:  python menu.py
ou via Flet:  flet run menu.py
"""

import sys
from pathlib import Path

# Permite rodar `python menu.py` sem precisar instalar o pacote (layout src/).
sys.path.insert(0, str(Path(__file__).parent / "src"))

import flet as ft

from pesqmed.views.menu import main

if __name__ == "__main__":
    ft.run(main, assets_dir="assets")
