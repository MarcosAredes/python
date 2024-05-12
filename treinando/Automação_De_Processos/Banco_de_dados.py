# lib
import sqlite3

# Criar BD
Conexao = sqlite3.connect("Banco_Dados.db")

# apontar
Cursor = Conexao.cursor()


# Criar uma tabela

Query = """

CREATE TABLE Tabela_Processamento(
    Id_Rotina TEXT,
    Nome_Rotina TEXT,
    Usuario TEXT,
    Maquina TEXT,
    Sistema_Operacional TEXT,
    Data_Inicio TEXT,
    Horario_Inicio TEXT,
    Teste_Conexao TEXT,
    IP_Local TEXT,
    Data_Termino TEXT,
    Horario_Termino TEXT,
    Tempo_Execução TEXT,
    Erro TEXT
)

"""

# Executar
Cursor.execute(Query)
Conexao.commit()


# fechar conexão
Conexao.close()
