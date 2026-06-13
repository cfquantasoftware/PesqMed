"""Testes de fumaça (smoke tests) para a tela de menu."""

import pesqmed
from pesqmed.config import APP_TITLE


def test_versao_definida():
    assert pesqmed.__version__


def test_titulo_app():
    assert APP_TITLE == "App PesqMed"


def test_view_menu_importavel():
    # Garante que o módulo da primeira tela importa sem erros.
    from pesqmed.views import menu

    assert callable(menu.main)
    assert callable(menu.build_layout)
