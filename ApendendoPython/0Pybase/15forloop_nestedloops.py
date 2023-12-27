# == for loop nested ===

# Outer loop = Loop de fora
# Inner loop = Loop de dentro

for number1 in range(5):
    print(number1)  # loop normal que imprime de 0 á 4
    for number2 in range(5):  # esse loop roda dentro do primeiro loop
        print(number2)

""" 
com o loop de dentro ele e confuso mas da para entender pois fica assim:

0 Esse 0 e do primeiro loop (Esse e o primeiro loop do Number1)
0 Esse e 0 e do segundo loop (Esse e o primeiro loop do Number2)
1 Esse e 1 e do segundo loop (Esse e o segundo  loop do Number2)
2 Esse e 2 e do segundo loop (Esse e o terceiro loop do Number2)
3 Esse e 3 e do segundo loop  (Esse e o quarto loop do Number2)
4 Esse e 4 e do segundo loop  (Esse e o quinto loop do Number2)
1 Esse e 1 e do primeiro loop  (Esse e o segundo loop do Number1)
Assim em diante

"""
