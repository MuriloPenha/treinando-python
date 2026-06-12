import os

tarefas = []

def exibir_titulo():
    print(""" 
    TAREFAS.COM - O SEU GERENCIADOR PREFERIDO!
    """)

def exibir_menu():
    print('1 - Adicionar tarefa')
    print('2 - Listar tarefas')
    print('3 - Marcar tarefa como concluída')
    print('4 - Remover tarefa')
    print('5 - Sair\n')

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def finalizar_app():
    exibir_subtitulo('Finalizar app')

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_nova_tarefa():
    exibir_subtitulo('Cadastro de novas tarefas')
    while True:
        nome_ja_existe = False
        nome_da_tarefa = input('Digite o nome da tarefa: ')
        for tarefa in tarefas:
         if nome_da_tarefa == tarefa['nome']:
            print('Já existe uma tarefa com esse nome, por favor escolha outro nome')
            nome_ja_existe = True
        if not nome_ja_existe:
            break
    descricao = input(f'Digite a descrição da tarefa {nome_da_tarefa}: ')
    dados_da_tarefa = {'nome':nome_da_tarefa, 'descricao':descricao, 'concluida':False}
    tarefas.append(dados_da_tarefa)
    print(f'A tarefa {nome_da_tarefa} foi cadastrada com sucesso!')

    voltar_ao_menu_principal()

def listar_tarefas():
    exibir_subtitulo('Listando tarefas')

    print(f'{'Nome da tarefa'.ljust(22)} | {'Descrição'.ljust(20)} | Status')
    for tarefa in tarefas:
        nome_tarefa = tarefa['nome']
        descricao = tarefa['descricao']
        concluida = 'concluída' if tarefa['concluida'] else 'pendente'
        print(f'- {nome_tarefa.ljust(20)} | {descricao.ljust(20)} | {concluida}')

    voltar_ao_menu_principal()

def alternar_estado_tarefa():
    exibir_subtitulo('ALterando estado da tarefa')
    nome_tarefa = input('Digite o nome da tarefa que deseja alterar o estado: ')
    tarefa_encontrada = False

    for tarefa in tarefas:
        if nome_tarefa == tarefa['nome']:
            tarefa_encontrada = True
            tarefa['concluida'] = not tarefa['concluida']
            mensagem = f'A tarefa {nome_tarefa} foi marcada como concluída' if tarefa['concluida'] else f'A tarefa {nome_tarefa} foi marcada como pendente'
            print(mensagem)

    if not tarefa_encontrada:
        print('A tarefa não foi encontrada')

    voltar_ao_menu_principal()


def remover_tarefa():
    exibir_subtitulo('Remover tarefa')
    nome_tarefa = input('Digite o nome da tarefa que deseja remover: ')
    tarefa_encontrada = False

    for tarefa in tarefas:
        if nome_tarefa == tarefa['nome']:
            tarefa_encontrada = True
            tarefas.remove(tarefa)
            print(f'A tarefa {nome_tarefa} foi removida com sucesso')

    if not tarefa_encontrada:
        print('A tarefa não foi encontrada')
    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1: 
            cadastrar_nova_tarefa()
        elif opcao_escolhida == 2: 
            listar_tarefas()
        elif opcao_escolhida == 3: 
            alternar_estado_tarefa()
        elif opcao_escolhida == 4: 
            remover_tarefa()
        elif opcao_escolhida == 5: 
            finalizar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_titulo()
    exibir_menu()
    escolher_opcao()

if __name__ == '__main__':
    main()