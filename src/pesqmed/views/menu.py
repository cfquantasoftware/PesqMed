"""Primeira tela do App PesqMed: menu principal com imagem de fundo."""

import sys
from pathlib import Path

import flet as ft

from pesqmed.config import APP_TITLE, LOGO

# Pasta assets/ na raiz do projeto (src/pesqmed/views/menu.py -> sobe 3 níveis)
ASSETS_DIR = str(Path(__file__).resolve().parents[3] / "assets")


def build_layout(page: ft.Page) -> ft.Control:
    """Constrói o layout da tela de menu. Separado de `main` para facilitar testes."""

    texto = ft.Text("Bem-vindo ao App PesqMed!", size=24, color="white")

    def abrir_inicio(e: ft.ControlEvent) -> None:
        texto.value = "Você clicou em Médicos Cadastrados"
        page.update()

    def abrir_config(e: ft.ControlEvent) -> None:
        texto.value = "Você clicou em Manter BD de Médicos"
        page.update()

    def sair(e: ft.ControlEvent) -> None:
        sys.exit()

    menu = ft.Column(
        controls=[
            ft.Button("Lista de Médicos", on_click=abrir_inicio),
            ft.Button("Manter BD", on_click=abrir_config),
            ft.Button("Sair", on_click=sair),
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.START,
        spacing=10,
    )

    return ft.Stack(
        expand=True,
        controls=[
            # Logo centralizada (maior, sem preencher a tela toda)
            ft.Container(
                expand=True,
                alignment=ft.Alignment(0, 0),
                content=ft.Image(src=LOGO, width=726, fit="contain"),
            ),
            # Camada escura
            ft.Container(expand=True, bgcolor="#80000000"),
            
            # Conteúdo principal
            ft.Row(
                expand=True,
                controls=[
                    ft.Container(content=menu, width=260, padding=20, bgcolor="#CCFFFFFF"),
                    ft.Container(
                        expand=True,
                        padding=20,
                        content=ft.Column(
                            controls=[texto],
                            alignment=ft.MainAxisAlignment.END,
                            horizontal_alignment=ft.CrossAxisAlignment.END,
                        ),
                    ),
                ],
            ),
        ],
    )


def main(page: ft.Page) -> None:
    page.title = APP_TITLE
    page.padding = 0
    page.spacing = 0
    page.add(build_layout(page))


def run() -> None:
    """Ponto de entrada: inicia o app Flet com a tela de menu."""
    ft.app(target=main, assets_dir=ASSETS_DIR)


if __name__ == "__main__":
    run()
