try:
    valor = int(input("Digite o valor do seu produto: "))
    print(valor)

except ValueError:
    print("Digitar apenas numeros")

else:
    print("Usuario digitou um valor correto")
    resultado = valor * 5
    print(resultado)


finally:
    print("codigo ok")
