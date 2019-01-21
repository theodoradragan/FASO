import dweepy
from grovepi import * 
from sendAlert import *
# Ca sera une bibliotheque pour gerer les temperatures et humidites : 
# detecter, sauvegarder, chercher et comparer
	
def detectTHInterieure():

	# Fonction qui retourne la temperature et l'humidite
	# Donnees : -
	# Resultat : Touple (humidite, temperature)

	dht_sensor_port = 3
	dht_sensor_type = 0
	[temperature, humidity] = dht(dht_sensor_port, dht_sensor_type)
	return [temperature,humidity]

def detectTHExterieure():

	# Fonction qui retourne la temperature et l'humidite
	# Donnees : -
	# Resultat : Touple (humidite, temperature)

	dht_sensor_port = 4
	dht_sensor_type = 0
	[temperature, humidity] = dht(dht_sensor_port, dht_sensor_type)
	return [temperature,humidity]


