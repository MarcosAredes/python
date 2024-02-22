cli = input("Qual cor tu quer?")
cores = ["amarelo", "vermelho", "azul", "roxo"]

if cli.lower() in cores:
    print("Tem sim")
else:
    print("Tem não ")
