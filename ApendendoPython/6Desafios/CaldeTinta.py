altura = int(input("Qual a altura da parede?"))
largura = int(input("Qual a largura da parede?"))
tinta = int(input("Qual rendimento da tinta?"))


def multiplicar():
    numero1 = altura
    numero2 = largura
    resultado = numero1 * numero2
    totalparede = resultado / tinta
    print(totalparede)


multiplicar()
