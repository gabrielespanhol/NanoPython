def perguntar():
    opcao = input("O que deseja realizar?\n"
                  "<I> - Para inserir um usuario\n"
                  "<P> _ Para pesquisar um usuario\n"
                  "<E> - Para Excluir um usuario\n"
                  "<L> - Para listar um usuario\n"
                  "<S> - Para Sair\n").upper()

    return opcao


def inserir(dicionario):
    chave = input("Digite o ID do usuario: ").upper()
    dicionario[chave] = [input("Digite o login"),
                         input("Digite o nome: ").upper(),
                         input("Digite a última data de acesso: "),
                         input("Qual a última estação acessada: ").upper()]

    print("Usuario: {} cadastrado com sucesso".format(dicionario.get(chave)))


def pesquisar(dicionario):
    opcao = input("Qual o login do usuario? ")
    if dicionario.get(opcao) is not None:
        print("Dados: {}".format(dicionario.get(opcao)))
    else:
        print("Usuario não encontrado")


def excluir(dicionario):
    opcao = input("Qual o nome do usuario a ser excluido: ")
    if dicionario.get(opcao) is not None:
        print("Usuario: {} \n foi excluido".format(dicionario.get(opcao)))
        del dicionario[opcao]
    else:
        print("Usuario não existe")


def listar(dicionario):
    i = 0
    for chave, valor in dicionario.items():
        print("Usuario")
        print("Login: ", chave)
        print("Dados: ", valor)
        i = +1
    if i == 0:
        print("Lista de usuarios vazia")
