

v = int(input('Qual valor do produto:'))

while v > 20:
    v = (v * 0.10) + v 
    print(f'O valor final do seu produto será de R$ {v}')
    break