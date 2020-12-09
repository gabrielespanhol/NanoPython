usuario = {}
resp = "S"
emails = []
while resp == "S":
    emails.append(input("Digite um email: ").lower())
    resp = input("Digite <S> para continuar: ").upper()

tupla = list(enumerate(emails))
for chave in range(0, len(tupla)):
    print("Email: {}".format(tupla[chave][1]))
    usuario[tupla[chave]] = [input("Digite o nome"), input("digite o nivel")]

for chave, dado in usuario.items():
    print("Usuario: {}".format(chave[0]))
    print("Email: {}".format(chave[1]))
    print("Nome: {}".format(dado[0]))
    print("Nivel: {}".format(dado[1]))

