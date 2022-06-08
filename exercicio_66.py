# ler varios numeros e mostrar a quantidade de numeros digitados e a soma deles
print("Digite 999 para sair\n")
n = int(input("Qual o número? "))
soma = 0
contador = 0
while n != 999:
    soma = soma + n
    contador += 1
    n = int(input("Qual o outro número? "))
print("A soma dos números é: {}".format(soma))
print("O número de números digitados foi: {}".format(contador))