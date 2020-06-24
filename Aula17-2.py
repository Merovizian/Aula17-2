# Adicionando listas em outras listas
lista_A = list()
lista_A.append("Gustavo")
lista_A.append(40)
lista_B = list()
lista_B.append(lista_A)
lista_A[0] = 'Maria'
lista_A[1] = 20
lista_B.append(lista_A)
print(lista_B)

# Adicionando listas usando [:]
lista_A = list()
lista_A.append("Gustavo")
lista_A.append(40)
lista_B = list()
lista_B.append(lista_A[:])
lista_A[0] = 'Maria'
lista_A[1] = 20
lista_B.append(lista_A[:])
print(lista_B)

# Criando Listas - Percorrendo os indices
galera = [['Joao',19],['Ana',33],['Joaquim',13],['Maria',45]]
for p, v in enumerate(galera):
    print(f"{v[0]:^10}tem {v[1]:^3}anos de idade.")

# Criando Listas com for
galera = list()
dado = list()
for c in range(0,3):
    dado.append(input("Nome: "))
    dado.append(int(input("Idade: ")))
    galera.append(dado[:])
    dado.clear()
print(galera)

