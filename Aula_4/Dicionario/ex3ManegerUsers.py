from Aula_4.Dicionario.ex4Fun import *
dicionario = {}

opcao = perguntar()

while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        inserir(dicionario)
    elif opcao == "P":
        pesquisar(dicionario)
    elif opcao == "E":
        excluir(dicionario)
    elif opcao == "L":
        listar(dicionario)
    opcao = perguntar()
