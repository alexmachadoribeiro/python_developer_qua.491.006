import flet as ft


def main(page: ft.Page):
    # função do evento
    def exibir_texto(e):
        result.value = texto.value
        page.update()

    # propriedades da página
    page.title = "Eventos"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT

    # variáveis
    texto = ft.TextField(label="Digite aqui o seu texto")
    result = ft.Text()

    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Text("App Evento", size=30, weight="bold"),
                alignment=ft.alignment.center,
            ),
            expand=True,
        ),
        texto,
        ft.ElevatedButton("Enviar", on_click=exibir_texto),
        result
    )


ft.app(main)
