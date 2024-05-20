# deixar ele sempre com "as ft" pois sempre tem q reverenciar ele ou seja "flet.algumacoisa" sendo "ft e melhor"
# Flet e um framework python para criação de apps Suporta python, Go,C#
# venv\Scripts\activate
# Para intalar ele é "pip install flet"
# Para executar ele é "flet run main.py"
# Para executar ele web é "flet run --web --port 8000 main.py"

import flet as ft
from models import Produto, session


def main(page: ft.Page):
    page.adaptive = True
    page.title = "Lojinha 123"

    lista_produtos = ft.ListView(expand=True)

    def cadastrar(e):
        try:
            novo_produto = Produto(titulo=produto.value, preco=float(preco.value))
            session.add(novo_produto)
            session.commit()
            print("Produto salvo com sucesso!")
            lista_produtos.controls.append(
                ft.Container(
                    ft.Text(f"Produto: {produto.value}, " " " f"Preço: {preco.value}"),
                    bgcolor=ft.colors.BLACK12,
                    padding=5,
                    alignment=ft.alignment.center,
                    margin=5,
                    border_radius=10,
                )
            )
            produto.value = ""
            preco.value = "0"

            txt_erro.visible = False
            txt_salvo.visible = True

        except:
            txt_erro.visible = True
            txt_salvo.visible = False

        page.update()

    txt_erro = ft.Container(
        ft.Text("Erro ao salvar o produto!!!"),
        visible=False,
        bgcolor=ft.colors.RED_300,
        padding=10,
        alignment=ft.alignment.center,
    )
    txt_salvo = ft.Container(
        ft.Text("Produto Salvo!!"),
        visible=False,
        bgcolor=ft.colors.GREEN_100,
        padding=10,
        alignment=ft.alignment.center,
    )

    txt_titulo = ft.Text("Titulo do produto:")
    produto = ft.TextField(
        label="Nome do Produto...",
        text_align=ft.TextAlign.LEFT,
        width=300,
        bgcolor=ft.colors.GREY_400,
    )

    txt_preço = ft.Text("Preço do produto")
    preco = ft.TextField(
        value="0",
        label="Digite o preço do produto",
        text_align=ft.TextAlign.LEFT,
        width=300,
        bgcolor=ft.colors.GREY_400,
    )

    bnt_produto = ft.ElevatedButton("Cadastrar", on_click=cadastrar)

    page.add(
        txt_salvo,
        txt_erro,
        txt_titulo,
        produto,
        txt_preço,
        preco,
        bnt_produto,
        lista_produtos,
    )

    for p in session.query(Produto).all():
        lista_produtos.controls.append(
            ft.Container(
                ft.Text(f"Produto: {p.titulo}, " " " f"Preço: {p.preco}"),
                bgcolor=ft.colors.BLACK12,
                padding=5,
                alignment=ft.alignment.center,
                margin=5,
                border_radius=10,
            )
        )

    page.update()


ft.app(target=main)
