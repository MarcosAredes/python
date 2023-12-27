#   Criar a classe
class Funcionarios:
    def __init__(self, nome, sobrenome, nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.nascimento = nascimento

    def dados(self):
        return self.nome + " " + self.sobrenome + " " + self.nascimento


#   Criar o Objeto


usuario1 = Funcionarios("Eleanor", "Rigby", "05/08/1966")
usuario2 = Funcionarios("mister", "postman", "05/08/1966")


#   Os dados não são passados diretamente na função, agora são associados aos parametros


# print
print(usuario1.dados())
