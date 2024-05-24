import flet as ft

def main(page: ft.Page):
    page.title = "App Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def diminuir(e):
        caixa_texto.value = str(int(caixa_texto.value) -1)
        page.update()

    def somar(e):
        caixa_texto.value = str(int(caixa_texto.value) +1)
        page.update()

    botao_menos = ft.IconButton(ft.icons.REMOVE, on_click=diminuir)
    caixa_texto = ft.TextField(value="0", width=100, text_align=ft.TextAlign.CENTER)
    botao_mais = ft.IconButton(ft.icons.ADD, on_click=somar)

    page.add(
        ft.Row(
            [botao_menos, caixa_texto, botao_mais], ft.MainAxisAlignment.CENTER
        )
    )

ft.app(target=main, view=ft.WEB_BROWSER)
