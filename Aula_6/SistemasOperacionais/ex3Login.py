# coding: iso-8859-1 -*-
import getpass

usuario = input("Digite o usu�rio: ").upper()
senha = getpass.getpass("Digite a senha: ")

if usuario == "BITMED" and senha == "FiAp1222":
    print("Usu�rio logado")
else:
    print("Login Negado")