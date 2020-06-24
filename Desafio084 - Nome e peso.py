print(f"\033[;1m{'Desafio 084 - Cadastrar nomes e pesos':*^70}\033[m")
# Inicializando a lista e os auxiliares.
pessoas = list()
pessoas_aux = list()
lista_menor = list()
lista_maior = list()
maior = menor = quantidade = 0

while True:
    # Pergunta o nome da pessoa e se o usuario quiser sair tem o break
    nome = input("Qual o nome: " if len(pessoas) == 0 else "Qual o nome [N para Sair]: ")
    if nome.strip().lower()[0] == 'n':
        break
    # coloca o nome digitado na lista auxiliar
    pessoas_aux.append(nome)
    # pergunta a idade e coloca na lista auxiliar
    idade = int(input(f"Qual o peso de {nome}: "))
    pessoas_aux.append(idade)
    # Coloca a lista auxiliar na lista principal e reseta a lista auxiliar
    pessoas.append(pessoas_aux[:])
    pessoas_aux.clear()
    # Coloca a primeira idade como sendo a menor
    if quantidade == 0:
        menor = idade
    quantidade += 1

# Retorna qual o menor peso
for p, c in enumerate(pessoas):
    if c[1] <= menor:
        menor = c[1]
# Retorna qual o maior peso
for p, c in enumerate(pessoas):
    if c[1] >= maior:
        maior = c[1]
# Retorna os nomes das pessoas com menor peso:
for p, c in enumerate(pessoas):
    if c[1] == menor:
        lista_menor.append(c[0])
# Retorna os nomes das pessoas com maior peso:
for p, c in enumerate(pessoas):
    if c[1] == maior:
        lista_maior.append(c[0])

print(f"Ao todo você cadastrou {quantidade} pessoas")
print(f"O maior peso foi de {maior}. Peso de {lista_maior}")
print(f"O menor peso foi de {menor}. Peso de {lista_menor}")


