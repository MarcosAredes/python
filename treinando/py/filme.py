import tkinter as tk
from tkinter import messagebox
import random

# Dicionário de filmes por gênero
filmes_por_genero = {
    "Ação": ["Matrix", "Vingadores", "John Wick", "Velozes e Furiosos", "Mad Max", "Duro de Matar", "Kill Bill", "Rambo"],
    "Aventura": ["Indiana Jones", "O Senhor dos Anéis", "Piratas do Caribe", "Jurassic Park", "Avatar", "Jumanji", "Harry Potter", "O Hobbit"],
    "Comédia": ["Se Beber, Não Case", "Superbad", "As Branquelas", "Ace Ventura", "Todo Mundo em Pânico", "Escola de Rock", "American Pie", "Meu Malvado Favorito"],
    "Drama": ["Forrest Gump", "O Poderoso Chefão", "Clube da Luta", "Cidadão Kane", "A Lista de Schindler", "Titanic", "Coração Valente", "A Origem"],
    "Fantasia": ["Harry Potter", "O Hobbit", "Cidade das Sombras", "A História sem Fim", "Labirinto", "As Crônicas de Nárnia", "Alice no País das Maravilhas", "Stardust"],
    "Terror": ["O Exorcista", "O Iluminado", "Invocação do Mal", "Psicose", "A Noite dos Mortos-Vivos", "Halloween", "O Chamado", "O Sexto Sentido"]
}

# Função para recomendar um filme baseado nos gêneros selecionados pelo usuário
def recomendar_filme(generos_preferidos):
    filmes_possiveis = []
    for genero in generos_preferidos:
        
        if genero in filmes_por_genero:
            filmes_possiveis.extend(filme.lower() for filme in filmes_por_genero[genero])  # Adiciona os filmes em minúsculas
    if filmes_possiveis:
        filme_recomendado = random.choice(filmes_possiveis).capitalize()  # Escolhe um filme aleatório e o converte para maiúscula
        return filme_recomendado
    else:
        return "Desculpe, não há filmes disponíveis para os gêneros selecionados."

# Função chamada quando o botão de recomendação é clicado
def recomendar():
    generos = entry_generos.get().split(",")
    filme_recomendado = recomendar_filme(generos)
    messagebox.showinfo("Recomendação de Filme", f"Recomendação de filme para você: {filme_recomendado}")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Recomendação de Filmes")

label_instrucao = tk.Label(root, text="Insira alguns gêneros de filmes de sua preferência (separados por vírgula):")
label_instrucao.pack()

entry_generos = tk.Entry(root)
entry_generos.pack()

botao_recomendar = tk.Button(root, text="Recomendar Filme", command=recomendar)
botao_recomendar.pack()

root.mainloop()

