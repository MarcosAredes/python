import tkinter as tk
from tkinter import messagebox
import random


class JogoDaVelha:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da veia")

        self.tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
        self.jogador_atual = "X"
        self.bot = "O"

        self.botoes = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.botoes[i][j] = tk.Button(
                    root,
                    text=" ",
                    font=("normal", 20),
                    width=5,
                    height=2,
                    command=lambda i=i, j=j: self.clique_botao(i, j),
                )
                self.botoes[i][j].grid(row=i, column=j)

    def reiniciar_jogo(self):
        self.tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
        self.jogador_atual = "X"

        for i in range(3):
            for j in range(3):
                self.botoes[i][j]["text"] = " "

    def clique_botao(self, linha, coluna):
        if self.tabuleiro[linha][coluna] == " ":
            self.tabuleiro[linha][coluna] = self.jogador_atual
            self.botoes[linha][coluna]["text"] = self.jogador_atual

            if self.verificar_vitoria(self.jogador_atual):
                messagebox.showinfo(
                    "Fim de Jogo",
                    f"Jogador {self.jogador_atual} Ganhou!",
                )
                self.reiniciar_jogo()
            elif self.tabuleiro_cheio():
                messagebox.showinfo("Fim de Jogo", "Empate!")
                self.reiniciar_jogo()
            else:
                self.jogador_atual = "O"
                self.jogada_bot()

    def jogada_bot(self):
        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j] == " ":
                    self.tabuleiro[i][j] = self.bot
                    self.botoes[i][j]["text"] = self.bot

                    if self.verificar_vitoria(self.bot):
                        messagebox.showinfo("Fim de Jogo", f"Bot venceu!")
                        self.reiniciar_jogo()
                        return
                    else:
                        self.jogador_atual = "X"
                        return

    def verificar_vitoria(self, jogador):
        # Verifica vitória nas linhas, colunas e diagonais
        for linha in self.tabuleiro:
            if all(c == jogador for c in linha):
                return True

        for coluna in range(3):
            if all(self.tabuleiro[i][coluna] == jogador for i in range(3)):
                return True

        if all(self.tabuleiro[i][i] == jogador for i in range(3)) or all(
            self.tabuleiro[i][2 - i] == jogador for i in range(3)
        ):
            return True

        return False

    def tabuleiro_cheio(self):
        # Verifica se o tabuleiro está cheio
        return all(all(c != " " for c in linha) for linha in self.tabuleiro)


if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoDaVelha(root)
    root.mainloop()
