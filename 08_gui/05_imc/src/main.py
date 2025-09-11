import flet as ft

def main(page: ft.Page):
    # função do evento
    def calcular_imc(e):
        if not peso.value:
            peso.error_text = "Peso não pode ficar vazio"
            page.update()
        else:
            peso.error_text = ""
            page.update()

        if not altura.value:
            altura.error_text = "Altura não pode ficar vazio"
            page.update()
        else:
            altura.error_text = ""

            # recebe os valores dos inputs
            peso.value = float(peso.value.replace(",", "."))
            altura.value = float(altura.value.replace(",", "."))

            # calcula o imc
            imc = peso.value/(altura.value**2)

            # exibe o valor do imc
            dlg_modal.title.value = f"Seu IMC é {imc:.2f}"

            # diagnóstico
            if imc < 18.5:
                dlg_modal.content.value = "Você está abaixo do peso."
            elif imc < 25:
                dlg_modal.content.value = "Você está no peso ideal."
            elif imc < 30:
                dlg_modal.content.value = "Você está acima do peso."
            elif imc < 35:
                dlg_modal.content.value = "Você está obeso."
            elif imc < 40:
                dlg_modal.content.value = "Você está com obesidade nível 2."
            else:
                dlg_modal.content.value = "Você está com obesidade mórbida."
            
            # abre o modal
            page.open(dlg_modal)

            # limpa e prepara os campos
            peso.value = ""
            altura.value = ""

            page.update()

    # propriedades da janela
    page.title = "Índice de Massa Corporal"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT

    # variáveis
    peso = ft.TextField(label="Peso", suffix_text="kg")
    altura = ft.TextField(label="Altura", suffix_text="metros", on_submit=calcular_imc)

    # caixa de diálogo
    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text(),
        content=ft.Text(size=20, weight="bold"),
        actions=[ft.TextButton("OK", on_click=lambda e: page.close(dlg_modal))],
        actions_alignment=ft.MainAxisAlignment.END
    )

    # barra superior
    page.appbar = ft.AppBar(title=ft.Text("IMC", size=16))

    # conteúdo da janela
    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Text("Índice de Massa Corporal", size=30, weight="bold"),
                alignment=ft.alignment.center
            ),
            expand=True
        ),
        ft.ResponsiveRow(
            [
                ft.Container(peso, col={"sm": 6, "md": 4, "xl": 2}),
                ft.Container(altura, col={"sm": 6, "md": 4, "xl": 2})
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                ft.Container(
                    ft.ElevatedButton("Calcular IMC", on_click=calcular_imc),
                    padding=30
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(main)
