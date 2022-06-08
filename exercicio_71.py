# simular caixa eletrônico
# perguntar valor a ser sacado
# dizer quantas cédulas de 50, 20, 10 e 1 serão entregues
import math

saque = int(input("Qual o valor a ser sacado? "))
notas_50 = math.floor(saque/50)
notas_20 = math.floor((saque % 50) / 20)
notas_10 = math.floor(((saque % 50) % 20)/ 10)
notas_1 = math.floor(((saque % 50) % 20) % 10)

print(f"Notas de 50: {notas_50}\nNotas de 20: {notas_20}\nNotas de 10: {notas_10}\nNotas de 1: {notas_1}")