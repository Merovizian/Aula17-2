print(f"\033[;1m{'Desafio 086 - Fazer uma matriz NxM':*^70}\033[m")
# Permite ao usuario criar a matriz do tamanho que quiser
l = int(input("Informe a quantidade de linhas: "))
c = int(input("Informer a quantidade de colunas: "))

# Alocando uma lista vazia com diversas listas dentro
matriz = ([],[],[],[],[],[],[])

# Gera a matriz percorrendo a linha e a coluna
for x in range(0,l):
    for y in range (0,c):
        numero = int(input(f"Digite o valor do elemento a{x+1}{y+1}: "))
        matriz[x].append(numero)

# percorre a matriz printando cada um de seus termos
for x in range(0, l ):
    for y in range(0, c ):
        print(f'{matriz[x][y]}',end=' ')
    print()



