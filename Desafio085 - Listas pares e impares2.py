print(f"\033[;1m{'Desafio 085 - Lista separada de pares e impares':*^70}\033[m")
# Cria uma lista com duas listas
lista = ([],[])

# Loop para criar numeros e separalos por pares ou impares
for x in range (0,7):
    numero = int(input("Digite um numero: "))
    if numero % 2 == 0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)

print(f"Os valores pares são {sorted(lista[0])}")
print(f"Os valores impares são {sorted(lista[1])}")
