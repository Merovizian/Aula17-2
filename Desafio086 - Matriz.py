print(f"\033[;1m{'Desafio 086 - Fazer uma matriz NxM':*^70}\033[m")
l = int(input("Informe a quantidade de linhas: "))
c = int(input("Informer a quantidade de colunas: "))
maior = 0

matriz = ([],[],[],[],[],[],[])


for x in range(0,l):
    for y in range (0,c):
        numero = int(input(f"Digite o valor do elemento a{x+1}{y+1}: "))
        matriz[x].append(numero)

for x in range(0, l ):
    for y in range(0, c ):
        print(f'{matriz[x][y]}',end=' ')
    print()



