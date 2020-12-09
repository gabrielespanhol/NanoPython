
with open("teste.txt", "r") as arquivo:
    conteudo = arquivo.readlines()
print("Tipo de dado da variavel", type(conteudo))
print("conteudo do arquivo: {}".format(conteudo))
