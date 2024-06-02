# bibliotecas
import random
import string


# variaveis da senha


def password_generator(len_pass=8):
    letras_options = string.ascii_letters
    numeros_options = string.digits
    pontos_options = string.punctuation
    opcao = letras_options + numeros_options + pontos_options
    senha_do_usuario = ""

    # processo de seleção/loop

    for i in range(0, len_pass):
        digit = random.choice(opcao)
        senha_do_usuario = senha_do_usuario + digit

    return senha_do_usuario


# Quantos digitos

choice_user = input("Quantos digitos na senha?")

if choice_user.isdigit():
    choice_user = int(choice_user)

else:
    print("Entrada inválida!")
    quit()

response = password_generator(len_pass=choice_user)
print(f"Senha gerada:\n{response}")
