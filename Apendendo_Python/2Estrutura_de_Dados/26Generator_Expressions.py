from sys import getsizeof

numeros = [x * 10 for x in range(1000)]
print(type(numeros))
print(getsizeof(numeros))

print("=================")

numeros = (x * 10 for x in range(1000))
print(type(numeros))
print(getsizeof(numeros))
