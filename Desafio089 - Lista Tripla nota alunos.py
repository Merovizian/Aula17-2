import time
print(f"\033[;1m{'Desafio 089 - Lista Tripla Com notas dos alunos':*^70}\033[m")
# Cria as listas vazias e auxiliares
alunos_lista = list()
alunos_quantidade = 0

# Cria um loop para o menu
while True:
    print('\n'*10)
    print("=-"*20,end='=\n')
    print(f"{'Menu Cadastro Alunos':^40}")
    print('''1 - Inserir novo aluno
2 - Menu de Notas
3 - Buscar por aluno
4 - Mostrar nomes
5 - Mostrar desempenho dos alunos
0 - Sair''')
    print("=-" * 20, end='=\n')
    escolha = int(input("Escolha a opção: "))
    # Caso o usuário crie uma função inválida o sistema retorna erro
    if escolha not in range(0,6):
        print("\033[1;31mOpção inválida!\033[m")
        input('Digite enter para continuar... ')
    # Escolha de saida do sistema de menu
    if escolha == 0:
        break
    # Cria a primeira lista, dentro da lista principal. Cada lista dessa tem informações sobre 1 aluno
    if escolha == 1:
        alunos_lista.append([[]])
        nome = input(f"Infome o nome do {alunos_quantidade+1}o aluno: ")
        alunos_lista[alunos_quantidade][0] = nome
        print(f'\033[1;32mO aluno {nome} foi adicionado com Sucesso!\033[m')
        alunos_lista[alunos_quantidade].append([])
        alunos_lista[alunos_quantidade].append(0)

        time.sleep(0.1)
        alunos_quantidade += 1


    if escolha == 2:
        print('\n' * 10)
        print("=-" * 20, end='=\n')
        print(f"{'MENU DE NOTAS':^40}")
        print('-' * 40)
        print(f"No {'Nome':<30} Notas")
        for x in range(0, alunos_quantidade):
            print(f"{(x+1):<3}{alunos_lista[x][0]:<30} {alunos_lista[x][1]}")

        alunos_matricula = int(input("Informe o No do aluno que queira adicionar as notas: "))
        if (alunos_matricula-1) < alunos_quantidade:
            if len(alunos_lista[alunos_matricula - 1][1]) != 0:
                print(f"\n\033[1;33m{'ANTEÇÂO!!':^40}\033[m")
                print(
                    f"O Aluno {alunos_lista[alunos_matricula - 1][0]} já possui as seguintes notas: {alunos_lista[alunos_matricula - 1][1]}")
                if (input("Deseja prosseguir mesmo assim? [N/S]: ")).lower()[0] in 's':
                    nota1 = input(f"Informe a primeira nota do aluno {alunos_lista[alunos_matricula - 1][0]}: ")
                    nota1 = float(nota1.replace(',', '.'))
                    nota2 = input(f"Informe a primeira nota do aluno {alunos_lista[alunos_matricula - 1][0]}: ")
                    nota2 = float(nota2.replace(',', '.'))
                    alunos_lista[alunos_matricula - 1][1] = (nota1, nota2)
                    alunos_lista[alunos_matricula - 1][2] = ((nota1 + nota2) / 2)
                else:
                    print("A nota do aluno não foi modificada!")
                    input("Pressione ENTER para continuar...")
            else:
                nota1 = input(f"Informe a primeira nota do aluno {alunos_lista[alunos_matricula-1][0]}: ")
                nota1 = float(nota1.replace(',','.'))
                nota2 = input(f"Informe a primeira nota do aluno {alunos_lista[alunos_matricula-1][0]}: ")
                nota2 = float(nota2.replace(',','.'))
                alunos_lista[alunos_matricula-1][1] = (nota1,nota2)
                alunos_lista[alunos_matricula-1][2] = ((nota1+nota2)/2)
        else:
            print("\033[1;31mMatricula Não Existe\033[m")
            time.sleep(1)



    if escolha == 3:
        auxiliar_menu3 = 0
        print('\n' * 10)
        print("=-" * 20, end='=\n')
        nome = (input("Informe ao menos 3 caracters: ")).lower()[:3]
        print(f"Procurando alunos com inicial {nome} no banco de dados..")
        time.sleep(1)
        for p, valor in enumerate(alunos_lista):
            if nome == str(valor[0]).lower()[0:3]:
                print(f"{valor[0]:<20} matricula {p+1}")
                auxiliar_menu3 = 1
        if auxiliar_menu3 == 0:
            print("Não existe o aluno informado no banco de dados.")
            time.sleep(2)
        else:
            input("Pressione ENTER para continuar...")

    # Mostra somente os nomes de todos os alunos
    if escolha == 4:
        print('\n' * 10)
        print("=-" * 20, end='=\n')
        print(f"{'ALUNOS CADASTRADOS':^40}")
        print('-' * 40)
        print(f"No {'Nome':<30}")

        for x in range(0, alunos_quantidade):
            print(f"{x+1:0>2} {alunos_lista[x][0]:<30}")
        input("Pressione ENTER para continuar ... ")

    # Mostra os nomes dos alunos e as medias
    if escolha == 5:
        print('\n' * 10)
        print("=-" * 20, end='=\n')
        print(f"{'ALUNOS CADASTRADOS':^40}")
        print('-' * 40)
        print(f"{'No':<3}{'Nome':<30} {'Média':>5}")
        for x in range (0,alunos_quantidade):
            if alunos_lista[x][2] <= 5:
                print(f"\033[1;31m{(x+1):0>2} {alunos_lista[x][0]:<30} {alunos_lista[x][2]:>5.2f}\033[m")
            elif alunos_lista[x][2] <= 7:
                print(f"\033[1;33m{(x+1):0>2} {alunos_lista[x][0]:<30} {alunos_lista[x][2]:>5.2f}\033[m")
            elif alunos_lista[x][2] <= 10:
                print(f"\033[1;32m{(x+1):0>2} {alunos_lista[x][0]:<30} {alunos_lista[x][2]:>5.2f}\033[m")

        input("Pressione ENTER para continuar ... ")



    '''input("Pressione ENTER para continuar ... ")'''










print(f"\n\033[1;34mObrigado por ter usado SoftEric")
print(alunos_lista)