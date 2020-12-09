# coding: iso-8859-1 -*-
inventario = {}
opcao = int(input("<1> para registrar ativo "
                  "\n<2> para persistir em arquivo "
                  "\n<3> para exibir ativo armazenado: "))

while 0 < opcao < 4:
    print(opcao)
    if opcao == 1:
        resp = "S"
        while resp == "S":
            chave = input("Digite o número patrimonial: ")
            inventario[chave] = [
                input("Digite a data da última atualização: "),
                input("Digite a descrição: "),
                input("Digite o departamento: ")]
            resp = input("Digite <S> para continuar.").upper()

    elif opcao == 2:
        with open("inventario.csv", "a") as inv:
            for chave, valor in inventario.items():
                inv.write("{};{};{};{} \n".format(chave, valor[0], valor[1], valor[2]))

                print("Persistido com sucesso!")

    elif opcao == 3:
        with open("inventario.csv", "r") as inv:
            print(inv.readline())

    opcao = int(input("<1> para registrar ativo "
                      "\n<2> para persistir em arquivo "
                      "\n<3> para exibir ativo armazenado: "))
