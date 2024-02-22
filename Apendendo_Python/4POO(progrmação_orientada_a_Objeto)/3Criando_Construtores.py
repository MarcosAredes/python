#   Criar a classe
class Funcionarios:
    def __init__(self, nome, sobrenome, nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.nascimento = nascimento


#   Criar o Objeto


usuario1 = Funcionarios("Eleanor", "Rigby", "05/08/1966")
usuario2 = Funcionarios("mister", "Rigby", "05/08/1966")


#   Criar os Parâmetros

'''
usuario1.nome = "Eleanor"
usuario1.sobrenome = "Rigby"
usuario1.nascimento = "05/08/1966"


usuario2.nome = "mister"
usuario2.sobrenome = "postman"
usuario2.nascimento = "04/09/1961"'''


#   Os dados não são passados diretamente na função, agora são associados aos parametros


# print
print(usuario1.nome)
print(usuario1.sobrenome)
print(usuario1.nascimento)

print("------------")

print(usuario2.nome)
print(usuario2.sobrenome)
print(usuario2.nascimento)
