inventario = []
resposta = "S"

while resposta == "S":
    equipamento = [input("nome: "),
                   int(input("Valor: ")),
                   int(input("serial: ")),
                   input("Departamento: ")]
    inventario.append(equipamento)

for elemento in inventario:
    print("Nome: ", elemento[0])
    print("Valor: ", elemento[1])
    print("Serial: ", elemento[2])
    print("Departamento: ", elemento[3])

busca = input("Digite o nome do equipamento que deseja buscar")
for elemento in inventario:
    if busca == elemento[0]:
        print("valor: ", elemento[1])
        print("Serial: ", elemento[2])

depreciacao = input("Informe o elemento que sera depreciado")
for elemento in inventario:
    if depreciacao == elemento[0]:
        elemento[1] = elemento[1] * 0.9

serial = int(input("Digite o numero serial do equipamento a ser removido"))
for elemento in inventario:
    if elemento[2] == serial:
        inventario.remove(elemento)


for elemento in inventario:
    print("Nome: ", elemento[0])
    print("Valor: ", elemento[1])
    print("Serial: ", elemento[2])
    print("Departamento: ", elemento[3])

valores = []
for elemento in inventario:
    valores.append(elemento[1])
if len(valores) > 0:
    print("O equipamento mais caro custa: ", max(valores))
    print("O equipamento mais barato custa: ", min(valores))
    print("O total de equipamentos é de: ", sum(valores))


