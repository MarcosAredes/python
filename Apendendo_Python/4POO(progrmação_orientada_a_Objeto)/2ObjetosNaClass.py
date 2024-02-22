#   Criar a classe
class Funcionarios:
    pass


#   Criar o Objeto


usuario1 = Funcionarios()
usuario2 = Funcionarios()


#   Criar os Parâmetros


usuario1.nome = "Eleanor"
usuario1.sobrenome = "Rigby"
usuario1.nascimento = "05/08/1966"


usuario2.nome = "mister"
usuario2.sobrenome = "postman"
usuario2.nascimento = "04/09/1961"


#   Os dados não são passados diretamente na função, agora são associados aos parametros


# print
print(usuario1.nome)
print(usuario1.sobrenome)
print(usuario1.nascimento)

print(usuario2.nome)
print(usuario2.sobrenome)
print(usuario2.nascimento)
