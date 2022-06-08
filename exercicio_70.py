# ler nome e preço de produtos
# perguntar se usuario quer continuar
# total gasto
# quantos produtos custam mais de 1000 reais
# nome do produto mais barato

gasto = 0
cont_1000 = 0
barato = 0
pro_bar = ""
cont = 0
while True:
    nome = str(input("Qual o nome do produto? "))
    preco = float(input("Qual o preço do produto? "))
    gasto = gasto + preco
    cont += 1
    if preco > 1000:
        cont_1000 += 1
    if cont == 1:
        barato = preco
    if preco < barato:
        barato = preco
        pro_bar = nome
    opcao = str(input("Você quer continuar? [S/N]: "))
    if opcao in "Nn":
        break

print(f"Total gasto: {gasto}\nNúmero de produtos acima de R$1000: {cont_1000}\nPreço do mais barato: {barato}\nNome do mais barato: {pro_bar}")