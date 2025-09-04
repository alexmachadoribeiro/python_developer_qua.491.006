import flet as ft
from dataclasses import dataclass

# classe Pessoa
@dataclass
class Pessoa:
    nome: str
    idade: int
    peso: float
    salario: float
    email: str

def main(page: ft.Page):
    # funação do evento
    def mostrar_dados(e):
        saida_titulo.value = "Dados do usuário:\n"
        nome.value = f"Nome: {usuario.nome.value}"
        idade.value = f"Idade: {usuario.idade.value}"
        peso.value = f"Peso: {usuario.peso.value} kg"
        salario.value = f"Salário: R$ {usuario.salario.value}"
        email.value = f"E-mail: {usuario.email.value}"

        page.update()

    # instancia a classe
    usuario = Pessoa(nome="", idade=0, peso=0.0, salario=0.0, email="")

    # propriedades da página
    page.title = "Dados do usuário"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT

    # seta os valores informados pelo usuário
    usuario.nome = ft.TextField(label="Nome")
    usuario.idade = ft.TextField(label="Idade", suffix_text="anos")
    usuario.peso = ft.TextField(label="Peso", suffix_text="kg")
    usuario.salario = ft.TextField(label="Salário", prefix_text="R$ ")
    usuario.email = ft.TextField(label="E-mail", on_submit=mostrar_dados)

    # variáveis de saída
    saida_titulo = ft.Text(weight="bold")
    nome = ft.Text()
    idade = ft.Text()
    peso = ft.Text()
    salario = ft.Text()
    email = ft.Text()

    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Text("Dados do usuário", size=30, weight="bold"),
                alignment=ft.alignment.center,
            ),
            expand=True,
        ),
        usuario.nome,
        usuario.idade,
        usuario.peso,
        usuario.salario,
        usuario.email,
        ft.ElevatedButton("Enviar", on_click=mostrar_dados),
        saida_titulo,
        nome,
        idade,
        peso,
        salario,
        email
    )

ft.app(main)
