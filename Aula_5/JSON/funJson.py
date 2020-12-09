# coding: iso-8859-1 -*-
import json
import os


def chamarMenu():
    escolha = int(input("Digite: "
                        "<1> para registrar ativo"
                        "<2> para exibir ativos armazenados: "))
    return escolha


def ler_arquivo(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, "r") as arq_json:
            dicionario = json.load(arq_json)
    else:
        dicionario = {}
    return dicionario


def gravar_arquivo(dicionario, arquivo):
    with open(arquivo, "w") as arq_json:
        json.dump(dicionario, arq_json)


def registrar(dicionario, arquivo):
    resp = "S"
    while resp == "S":
        dicionario[input("Digite o n�mero patrimonial: ")] = [
            input("Digite a data da �ltima atualiza��o: "),
            input("Digite a descri��o: "), input("Digite o departamento: ")]
        resp = input("Digite <S> para continuar.").upper()
        gravar_arquivo(dicionario, arquivo)
    return "JSON gerado!!!!"


def exibir(arquivo):
    dicionario = ler_arquivo(arquivo)
    for chave, dado in dicionario.items():
        print("Data.........: ", dado[0])
        print("Descri��o....: ", dado[1])
        print("Departamento.: ", dado[2])
