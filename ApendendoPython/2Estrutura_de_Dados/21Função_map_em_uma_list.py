lista1 = [1, 2, 3, 4]


def multi(x):
    return x * 2


lista2 = map(multi, lista1)

print(list(lista2))
