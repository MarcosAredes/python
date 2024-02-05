import time
import random

class MedidorRPM:
    def __init__(self):
        self.rpm = 0

    def medir_rpm(self):
        # Simulação: gera um número aleatório como RPM
        self.rpm = random.randint(800, 4000)

    def exibir_informacoes(self):
        print(f"RPM: {self.rpm}")
        print("------")

# Instanciar o objeto MedidorRPM
medidor_rpm = MedidorRPM()

try:
    while True:
        # Simulação: medir RPM
        medidor_rpm.medir_rpm()

        # Exibir informações do medidor de RPM
        medidor_rpm.exibir_informacoes()

        # Aguardar um curto período de tempo (simulando a leitura em intervalos)
        time.sleep(1)

except KeyboardInterrupt:
    print("Programa encerrado pelo usuário.")
