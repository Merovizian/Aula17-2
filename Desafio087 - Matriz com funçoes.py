print(f"\033[;1m{'Desafio 086 - Fazer uma matriz NxM':*^70}\033[m")
# Permite ao usuario criar a matriz do tamanho que quiser
l = int(input("Informe a quantidade de linhas: "))
c = int(input("Informer a quantidade de colunas: "))

maior = maior_numero = soma_par = soma_coluna = 0
matriz = list()

# Alocando uma lista vazia e cria as linhas de acordo com o usuario
for x in range(0,l):
    matriz.append([])

# Gera a matriz percorrendo a linha e a coluna e já soma os pares e verifica o maior algarismo
for x in range(0,l):
    for y in range (0,c):
        numero = int(input(f"Digite o valor do elemento a{x+1}{y+1}: "))
        matriz[x].append(numero)
        if numero % 2 == 0:
            soma_par += numero
        if numero > maior_numero:
            maior_numero = numero

# Serve para colocar 0 antes dos numeros para uma visualização melhor
if maior_numero < 10:
    maior_numero = 1
elif maior_numero < 100:
    maior_numero = 2
elif maior_numero < 1000:
    maior_numero = 3


# percorre a matriz printando cada um de seus termos
for x in range(0, l ):
    for y in range(0, c ):
        print(f'{matriz[x][y]:0>{maior_numero}}',end=' ')
    print()


# Permite o usuario informar a coluna e soma os termos dessa coluna
coluna = int(input("Informe a coluna que queira somar: "))
for x in range(0, l):
    soma_coluna += (matriz[x][coluna-1])

# Permite o usuario informar a linha e procura o maior valor dessa linha
linha = int(input("Informe a linha que queira o maior valor: "))
for x in range(0, l):
    for y in range(0,c):
        if matriz[linha-1][y] >= maior:
            maior = matriz[linha-1][y]

print(f"A soma de todos os numeros pares é: {soma_par}")
print(f"A soma dos elementos da coluna {coluna} é: {soma_coluna}")
print(f"O maior valor da linha {linha} é {maior}")


