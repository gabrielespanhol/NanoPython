from geopy.geocoders import Nominatim

geolocalizacao = Nominatim(user_agent="wazeyes")  # nome do seu aplicativo
# location = geolocalizacao.geocode("175 5th Avenue NYC")
# location = geolocalizacao.geocode("Av Horacio Barione Sao bernardo do campo 211")
location = geolocalizacao.geocode("Av Aricanduva Ouro fino")
print(location.address)
print((location.latitude, location.longitude))

