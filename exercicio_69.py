# ler sexo e idade de varias pessoas
# perguntar se deve ou nao continuar
# mostrar quantas pessoas têm mais de 18 anos
# quantos homens
# quantas mulheres têm menos de 20 anos
opcao = "S"
cont_18 = 0
cont_hom = 0
cont_mul = 0
while True:
    idade = int(input("Qual a sua idade? "))
    sexo = str(input("Qual o seu sexo? [M/F]")).upper().strip()
    while sexo != "M" and sexo != "F":
        sexo = str(input("Qual o seu sexo? [M/F]")).upper().strip()
    if idade > 18:
        cont_18 += 1
    if sexo in "Mm":
        cont_hom += 1
    if sexo in "Ff":
        if idade < 20:
            cont_mul += 1
    opcao = str(input("Você deseja continuar? [S/N]: "))
    if opcao in "Nn":
        break

print(f" {cont_18} pessoas têm mais de 18 anos, {cont_hom} homens se cadastraram e {cont_mul} mulheres têm menos de 20 anos.")


