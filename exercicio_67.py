# tabuada e será interrompido se digitar valor negativo
contador = 1
n = 0
multi = 0
while True:
    n = int(input("Digite um número: "))
    if n < 0:
        break
    while contador < 11:
        multi = n * contador
        print("-=" * 20)
        print(f"{n} x {contador} = {multi}")
        contador += 1
    contador = 1