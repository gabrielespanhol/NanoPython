# coding: iso-8859-1 -*-
with open("pagina.html", "w") as pagina:
    pagina.write("<body> <h1> Esta � um teste para p�gina WEB </h1>")
    pagina.write("<br><h2> Abaixo seguem alguns nomes:  </h2>")
    pagina.write("<h3>")
    nome = ""
    while nome != "SAIR":
        nome = input("Digite um nome ou SAIR: ").upper()
        if nome != "SAIR":
            pagina.write("<br>" + nome)

    pagina.write("</h3></body>")
