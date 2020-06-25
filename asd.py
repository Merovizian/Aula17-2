lista = list()
notas_lista = list()
quantidade = 0
while quantidade < 3:
    lista.append([[]])
    nome = input("Informe o nome do aluno: ")
    lista[quantidade][0] = nome
    nota1 = float(input(f"infome a primeira nota de {lista[quantidade][0]}: "))
    nota2 = float(input(f"infome a segunda nota de {lista[quantidade][0]}: "))
    lista[quantidade].append([nota1,nota2])
    lista[quantidade].append((nota1+nota2)/2)
    quantidade += 1
    print(lista)

print(lista[2])