# coding: iso-8859-1 -*-
from geopy.geocoders import *

geolocalizacao = Nominatim(user_agent="wazeyes")

endereco = input("Digite um endereço com numero e cidade")

resultado = geolocalizacao.geocode(endereco)
if resultado.valid_address:
    print("Endereço completo: {}".format(resultado))
    print("Coordenadas: {}".format(resultado.coordinates))
    print("Numero: {}".format(resultado.street_number))
    print("CEP: {}".format(resultado.postal_code))

print("foi encontrado {} endereço(s)" .format(resultado.count))
for r in resultado:
    print("Cidade: {}".format(r.state))
    print("pais: {}".format(r.country))
    print("logradouro: {}".format(r.route))
    print("-----------------------------")
