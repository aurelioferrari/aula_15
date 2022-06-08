import random
pc = 0
jogador = 0
opcao = ""
soma = 0
resto = 0
contador = 0
while True:
    pc = random.randint(0, 5)
    jogador = int(input("Escolha um número: "))
    opcao = str(input("Par[P] ou ímpar[I]: ")).upper().strip()
    while opcao != "P" and opcao != "I":
        opcao = str(input("Par[P] ou ímpar[I]: ")).upper().strip()
    if opcao in "Pp":
        soma = pc + jogador
        if soma %2 == 0:
            print("Você ganhou!")
            contador += 1
        else:
            print(f"Você perdeu, mas ganhou {contador} partidas consecutivas")
            break
    if opcao in "Ii":
        soma = pc + jogador
        if soma %2 == 1:
            print("Você ganhou!")
            contador += 1
        else:
            print(f"Você perdeu, mas ganhou {contador} partidas consecutivas")
            break
