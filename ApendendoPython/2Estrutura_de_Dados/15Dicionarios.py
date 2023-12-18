# Dicionário vazio
meu_dicionario = {}

# Dicionário com alguns itens
pessoa = {"nome": "Alice", "idade": 30, "cidade": "Wonderland"}

# Acessando valores usando chaves
nome = pessoa["nome"]
idade = pessoa["idade"]
print(nome, idade)

# Adicionando um novo par chave-valor
pessoa["profissao"] = "Programadora"

# Modificando um valor existente
pessoa["idade"] = 31

# Removendo um item por chave
del pessoa["cidade"]

# Usando o método pop para remover e obter o valor
profissao = pessoa.pop("profissao")

# Verificando se uma chave existe
existe_cidade = "cidade" in pessoa

# Obtendo todas as chaves
chaves = pessoa.keys()

# Obtendo todos os valores
valores = pessoa.values()

# Obtendo pares chave-valor como tuplas
itens = pessoa.items()

# Iterando sobre chaves
for chave in pessoa:
    print(chave)

# Iterando sobre valores
for valor in pessoa.values():
    print(valor)

# Iterando sobre pares chave-valor
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

# Dicionário aninhado
contato = {
    "telefone": {"casa": "123-456", "trabalho": "789-012"},
    "email": "alice@example.com",
}
