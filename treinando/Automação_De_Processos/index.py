# frameworks

# lib(data e hora)
import datetime

# lib (sistema operacional)
import os
import platform
import win32com.client as win32

# lib para internet
import requests
import socket

# ignorar avisos
import warnings

warnings.filterwarnings("ignore")


# Pandas
import pandas as pd

# Lib para API Yahoo finance
import yfinance as yf
import pandas_datareader.data as web

# Matplotlib
import matplotlib.pyplot as plt

# SQL
import sqlite3


# Nome Rotinas

Id_Rotina = 1
Nome_Rotina = "Fluxo de dados"

# identificar o usuario


# Função de identificação de Usuario
def Identificando_Usuario():

    # Capturar o User
    Usuario = os.environ.get("USERNAME")

    # Capturar a maquina
    Maquina = platform.node()

    # Capturar o Os(Sistema Operacional)
    Os = platform.platform()

    # Retorno da Função
    return (Usuario, Maquina, Os)


# Identificar o Inicio
def Inicio_Rotina():

    # data de inicio
    Data_inicio = datetime.datetime.today().date()

    # Hora de inicio
    Hora_inicio = datetime.datetime.now()

    # retorno
    return (Data_inicio, Hora_inicio)


# Identificar o Término
def Termino_Rotina():

    # data de término
    Data_termino = datetime.datetime.today().date()

    # Hora de término
    Hora_termino = datetime.datetime.now()

    # retorno
    return (Data_termino, Hora_termino)


# Identificar a conexão de Internet
def Verificar_Conexao():

    # Conexão

    URL = "https://www.google.com"

    # tempo de conexão
    Timeout = 5

    try:
        # função para
        requests.get(URL, timeout=Timeout)
        return True

    except:
        return False


# Identificar o IP =)
def Identificando_IP():

    try:
        # indentificando o IP local
        IP_Local = socket.gethostbyname(socket.gethostname())
        return IP_Local

    except:
        return False


# Colocar todos os erros q acontecer nos processos
Erro_Operacional = ""

# Gerando os paramentros
Lista_User = Identificando_Usuario()
Lista_Inicio = Inicio_Rotina()
Conexao_Internet = Verificar_Conexao()
Verificando_IP = Identificando_IP()

"""print(
    Lista_User,
    Lista_Inicio,
    Lista_Termino,
    Conexao_Internet,
    Verificando_IP,
    Erro_Operacional,
)"""

# Operacional
""" Quando quiser automatizar uma tarefa coloca aqui"""

# Termino da rotina
Lista_Fim = Termino_Rotina()


# Organização

Dicionario = {
    "Id_Rotina": Id_Rotina,
    "Nome_Rotina": Nome_Rotina,
    "Usuario": Lista_User[0],
    "Maquina": Lista_User[1],
    "Sistema_Operacional": Lista_User[2],
    "Data_Inicio": Lista_Inicio[0],
    "Horario_Inicio": Lista_Inicio[1],
    "Teste_Conexao": Conexao_Internet,
    "IP_Local": Verificando_IP,
    "Data_Termino": Lista_Fim[0],
    "Horario_Termino": Lista_Fim[1],
    "Tempo_Execução": (Lista_Fim[1] - Lista_Inicio[1]),
    "Erro": Erro_Operacional,
}

# Tab Log
Tabela_Log = pd.DataFrame(Dicionario, index=[0])


# Fazer a conexão com SQL

# Criar Conexão
Conexao = sqlite3.connect("Banco_Dados.db")

# Apontar
Cursor = Conexao.cursor()

# Enviar infos

Tabela_Log.to_sql(
    # Nome da tabela
    "Tabela_Processamento",
    # Conexao
    Conexao,
    # Se a tabela existe
    if_exists="append",
    # Ignorar o index
    index=False,
)

# Pandas
pd.read_sql(
    # Query
    "SELECT* FROM Tabela_Processamento",
    # Conexao
    Conexao,
)
