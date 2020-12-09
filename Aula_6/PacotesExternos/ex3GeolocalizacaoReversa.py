# coding: iso-8859-1 -*-
from geopy.geocoders import Nominatim
geo = Nominatim(user_agent="wazeyes")

latitude = float(input("Digite a latitude: "))
longitude = float(input("Digite a longitude: "))

resultado = geo.reverse(f"{latitude}, {longitude}")
# if resultado.valid_address:
print("endereço completo: {}" .format(resultado))
print("numero: {}".format(resultado.street_number))
print("CEP: {}".format(resultado.postal_code))
