"""
idade = int(input('Qual sua idade ?'))

if  idade >= 16:
    print('Pode votar!')
elif idade <= 15:
    print('Não pode votar')
"""

idade = int(input("Qual sua idade ?"))
resultado = "Pode votar!" if idade >= 16 else "Não pode votar"

print(resultado)
