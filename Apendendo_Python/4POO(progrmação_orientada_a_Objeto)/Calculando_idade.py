from datetime import datetime


# Criar a classe
class Funcionario:
    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = int(ano_nascimento)

    def dados(self):
        return f"{self.nome} {self.sobrenome} {self.ano_nascimento}"

    def idade_funcionario(self):
        ano_atual = datetime.now().year
        idade = ano_atual - self.ano_nascimento
        return idade


# Criar os objetos

usuario1 = Funcionario("Eleanor", "Rigby", "1966")
usuario2 = Funcionario("Mister", "Postman", "1961")


# Chamar o método idade_funcionario nos objetos

idade_usuario1 = usuario1.idade_funcionario()
idade_usuario2 = usuario2.idade_funcionario()


# Exibir as idades
print(f"A idade do {usuario1.nome} {usuario1.sobrenome} é: {idade_usuario1} anos")
print(f"A idade do {usuario2.nome} {usuario2.sobrenome} é: {idade_usuario2} anos")
