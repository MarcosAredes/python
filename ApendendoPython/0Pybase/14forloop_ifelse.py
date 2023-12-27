# For loop com If e Else

compra_confirmada = True
dados_compra = "compra no valor de 2.500"


for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print("compra realizada")
        break

else:
    compra_confirmada = False
    print("Falhou ou tá dando golpe?")
"""
No caso if e else você coloca o if dentro do for se ele for verdade ele 
para de rodar e envia os dados
mas se for mentira ele pula para o else
"""
