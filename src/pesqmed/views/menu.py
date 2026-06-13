"""Primeira tela do App PesqMed: menu principal com imagem de fundo."""

import sys

import flet as ft

from pesqmed.config import APP_TITLE, LOGO


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
            # Imagem de fundo
            ft.Image(src=LOGO, fit="cover", expand=True),
            # Camada escura
            ft.Container(expand=True, bgcolor="#80000000"),
            # Marca d'água (canto superior direito)
            ft.Container(
                alignment=ft.Alignment(1, -1),
                padding=20,
                content=ft.Image(src=LOGO, width=120, opacity=0.6),
            ),
            # Conteúdo principal
            ft.Row(
                expand=True,
                controls=[
                    ft.Container(content=menu, width=260, padding=20, bgcolor="#CCFFFFFF"),
                    ft.Container(
                        expand=True,
                        content=ft.Column(
                            controls=[texto],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
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
