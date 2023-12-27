# 1
conjunto = {1, 2, 3, 4, 5}
tamanho = len(conjunto)
print(tamanho)  # Saída: 5

# 2
conjunto = {1, 2, 3}
conjunto.add(4)
print(conjunto)  # Saída: {1, 2, 3, 4}

# 3
conjunto = {1, 2, 3, 4}
conjunto.remove(3)
print(conjunto)  # Saída: {1, 2, 4}

# 4
conjunto = {1, 2, 3, 4}
conjunto.discard(3)
print(conjunto)  # Saída: {1, 2, 4}

# 5
conjunto = {1, 2, 3, 4}
elemento_removido = conjunto.pop()
print(elemento_removido, conjunto)

# 6
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
uniao = conjunto1.union(conjunto2)
print(uniao)  # Saída: {1, 2, 3, 4, 5}

# 7
conjunto1 = {1, 2, 3, 4}
conjunto2 = {3, 4, 5, 6}
intersecao = conjunto1.intersection(conjunto2)
print(intersecao)  # Saída: {3, 4}

# 8
conjunto1 = {1, 2, 3, 4}
conjunto2 = {3, 4, 5, 6}
diferenca = conjunto1.difference(conjunto2)
print(diferenca)  # Saída: {1, 2}

# 9
conjunto = {1, 2, 3, 4}
conjunto.clear()
print(conjunto)  # Saída: set()
