equipamentos = []
valor = []
numero_serial = []
departamento = []

resposta = "S"

while resposta == "S":
    equipamentos.append(input("digite o equipamento: "))
    valor.append(float(input("digite o valor: ")))
    numero_serial.append(int(input("Digite o numero serial: ")))
    departamento.append(input("Digite o departamento: "))
    resposta = input("Digite 'S' para continuar: ").upper()


for indice in range(0, len(equipamentos)):
    print("Equipamento: ", (indice+1))
    print("Nome: ", equipamentos[indice])
    print("Valor: ", valor[indice])
    print("Numero Serial: ", numero_serial[indice])
    print("departamento: ", departamento[indice], "\t")


busca = input("Digite o nome do equipamento: ")
for i in range(0, len(equipamentos)):
    if busca == equipamentos[i]:
        print("Valor: ", valor[i])
        print("Numero de Serie", numero_serial[i])


busca = input("Digite o nome do equipamento que sofreu depreciação: ")
for i in range(0, len(equipamentos)):
    if busca == equipamentos[i]:
        print("Valor antes do desconto", valor[i])
        valor[i] = valor[i]*0.9
        print("valor apos o desconto", valor[i])

busca = int(input("Digite o numero de serie do equipamento a ser removido: "))
for i in range(0, len(equipamentos)):
    if busca == numero_serial[i]:
        del equipamentos[i]
        del valor[i]
        del numero_serial[i]
        del departamento[i]
        break


for indice in range(0, len(equipamentos)):
    print("Nome: ", equipamentos[indice])
    print("Valor: ", valor[indice])
    print("Numero Serial: ", numero_serial[indice])
    print("departamento: ", departamento[indice], "\t")