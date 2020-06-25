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

    # Cria a primeira lista, dentro da lista principal. No formato: [[Aluno,[nota1,nota2],Media, ...]
    if escolha == 1:
        alunos_lista.append([[]])
        nome = input(f"Infome o nome do {alunos_quantidade+1}o aluno: ")
        # Coloca o nome do aluno(indice 0) da lista atual(alunos_quantidade)
        alunos_lista[alunos_quantidade][0] = nome
        # Inicia também a lista de notas(indice 1) e a media(indice 2)
        alunos_lista[alunos_quantidade].append([])
        alunos_lista[alunos_quantidade].append(0)
        print(f'\033[1;32mO aluno {nome} foi adicionado com Sucesso!\033[m')
        time.sleep(1.5)
        alunos_quantidade += 1

    # Menu responsavel por manipular as notas
    if escolha == 2:
        print('\n' * 10)
        print("=-" * 20, end='=\n')
        print(f"{'MENU DE NOTAS':^40}")
        print('-' * 40)
        print(f"No {'Nome':<30} Notas")
        # loop para mostrar os alunos(indice 0) e suas notas(indice 1).
        for x in range(0, alunos_quantidade):
            print(f"{(x+1):<3}{alunos_lista[x][0]:<30} {alunos_lista[x][1]}")
        # pergunta ao usuario qual o aluno que quer adicionar nota
        alunos_matricula = int(input("Informe o No do aluno que queira adicionar as notas: "))
        # if para verificar se o aluno digitado existe.
        if (alunos_matricula-1) < alunos_quantidade:
            # Caso exista o aluno o programa analiza se o aluno já possui nota registrada se sim, mostra um aviso e as notas na tela
            if len(alunos_lista[alunos_matricula - 1][1]) != 0:
                print(f"\n\033[1;33m{'ANTEÇÂO!!':^40}\033[m")
                print(f"O Aluno {alunos_lista[alunos_matricula - 1][0]} já possui as seguintes notas: {alunos_lista[alunos_matricula - 1][1]}")
                # Pergunta ao usuario se ele quer modificar as notas já existentes
                if (input("Deseja prosseguir mesmo assim? [N/S]: ")).lower()[0] in 's':
                    nota1 = input(f"Informe a primeira nota do aluno {alunos_lista[alunos_matricula - 1][0]}: ")
                    # Metodo para trocar a virgula (usualmente usada por usuarios) por pontos
                    nota1 = float(nota1.replace(',', '.'))
                    nota2 = input(f"Informe a primeira nota do aluno {alunos_lista[alunos_matricula - 1][0]}: ")
                    nota2 = float(nota2.replace(',', '.'))
                    # Coloca as notas digitadas nos devidos nos devidos locais(indice 1) e coloca a media no devido local (indice 2)
                    alunos_lista[alunos_matricula - 1][1] = [nota1, nota2]
                    alunos_lista[alunos_matricula - 1][2] = ((nota1 + nota2) / 2)
                # Caso o usuario não queira sobrescrever as notas já existentes
                else:
                    print("A nota do aluno não foi modificada!")
                    input("Pressione ENTER para continuar...")
            # Else se caso o usuario não tiver nenhuma nota registrada.
            else:
                # mesmo processo de adição utilizado acima
                nota1 = input(f"Informe a primeira nota do aluno {alunos_lista[alunos_matricula-1][0]}: ")
                nota1 = float(nota1.replace(',','.'))
                nota2 = input(f"Informe a primeira nota do aluno {alunos_lista[alunos_matricula-1][0]}: ")
                nota2 = float(nota2.replace(',','.'))
                alunos_lista[alunos_matricula-1][1] = [nota1,nota2]
                alunos_lista[alunos_matricula-1][2] = ((nota1+nota2)/2)
        # Else do verificador de matricula, caso não exista matricula
        else:
            print("\033[1;31mMatricula Não Existe\033[m")
            time.sleep(1)

    # Menu que busca os alunos.
    if escolha == 3:
        # auxiliar para buscas
        auxiliar_menu3 = 0
        print('\n' * 10)
        print("=-" * 20, end='=\n')
        # Da a opção por procurar com apenas 3 caracteres
        nome = (input("Informe ao menos 3 caracteres: ")).lower()[:3]
        print(f"Procurando alunos com inicial {nome} no banco de dados..")
        time.sleep(1)
        # faz uma busca na lista para ver se os 3 caracteres existe em algum nome
        for p, valor in enumerate(alunos_lista):
            if nome == str(valor[0]).lower()[0:3]:
                print(f"{valor[0]:<20} matricula {p+1}")
                auxiliar_menu3 = 1
        # O auxiliar informa se o nome foi encontrado ou nao
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
        # for para criar a lista de alunos cadastrados pela matricula (indice da lista principal) e pelo nome (indice 0)
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
        # loop para printar os nomes(indice 0) e as medias(indice 2).
        for x in range (0,alunos_quantidade):
            # Cria uma cor de acordo com a media.
            if alunos_lista[x][2] <= 5:
                print(f"\033[1;31m{(x+1):0>2} {alunos_lista[x][0]:<30} {alunos_lista[x][2]:>5.2f}\033[m")
            elif alunos_lista[x][2] <= 7:
                print(f"\033[1;33m{(x+1):0>2} {alunos_lista[x][0]:<30} {alunos_lista[x][2]:>5.2f}\033[m")
            elif alunos_lista[x][2] <= 10:
                print(f"\033[1;32m{(x+1):0>2} {alunos_lista[x][0]:<30} {alunos_lista[x][2]:>5.2f}\033[m")
        input("Pressione ENTER para continuar ... ")

print(f"\n\033[1;34mObrigado por ter usado SoftEric")
print(alunos_lista)