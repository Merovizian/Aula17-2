import random , time

print(f"\033[;1m{'Desafio 088 - Jogos da megasena com numeros aleatorios':*^70}\033[m")
# Declaração das variaveis utilizadas
lista = list()
dados = list()
numero = 0

# Cria o layout e pergunta a quantidade de jogos
print("=-"*20,end='=')
print(f"\n{'JOGO DA MEGA SENA':^40}")
print("=-"*20,end='=')
jogos = int(input("\nInforme a quantidade de jogos que deseja fazer: "))
print()
print("=-"*5,end='=')
print(f" Sorteando {jogos} Jogos ",end='')
print("=-"*5,end='=\n')

# loop para rodar a lista dos jogos
for x in range(0,jogos):
    for y in range(0,6):
       #  gera um numero aleatorio entre 1 e 60
       numero = random.randint(1,60)
       # loop para verificar se o numero gerado esta la lista
       while numero in dados:
           # se o numero gerado estiver na lista, cria-se um novo
           numero = random.randint(1,60)
       #  Depois de garantido que o numero não esta na lista, adiciona esse numero em uma lista auxiliar
       dados.append(numero)
    # Copia 1 jogo criado na lista de jogoS e deleta o conteudo a lista auxiliar
    lista.append(dados[:])
    dados.clear()


# loop para printar os jogos criados.
for k in range(0,jogos):
    time.sleep(1)
    print(f"Jogo {k+1}: {lista[k]}")
print("=-"*20,end='=\n')
