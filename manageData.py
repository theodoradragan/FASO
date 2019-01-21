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

def saveTH(temperature,humidite):
	
	# Fonction qui cree et envoie un tweet avec la temperature 
	# et l'humidite actuelles de cette heure.
	# Donnees : temperature : float, humidite : float
	# Resultat : -
	
	dweepy.dweet_for('Assistant', {'Temperature' : temperature, 'Humidite' : humidite})

def loadTH(heure):
	
	# Fonction qui donne la temperature et humidite d'une heure,
	# stockees en forme de dweet.
	# Donnees : heure : float
	# Resultat : Tuple (temperature,humidite)

	dweeps = dweepy.get_dweets_for('Assistant')
	resDweep = dweepy[0]['content']['Temperature']

	for dweep in dweeps:
		created = dweep['created']
		created_string = str(cr)
		heureDweep = (((s.split('T'))[1]).split(':'))[0]
		minute = (((s.split('T'))[1]).split(':'))[1]
		if (heure == heureDweep):
			resDweep = dweep

	return (resDweep['content']['Temperature'] , resDweep['content']['Humidite'])
	


if __name__ == '__main__':
	[t, h] = detectTH()
	print(t,h)
	saveTH(11,22)
