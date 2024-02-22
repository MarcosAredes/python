try:
    valor = int(input("Digite o valor do seu produto: "))
    print(type(valor))

except ValueError:
    print("Digitar apenas numeros")
