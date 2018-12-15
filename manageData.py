import dweepy
#import Adafruit_DHT
from grovepi import * 
# Ca sera une bibliotheque pour gerer les temperatures et humidites : 
# detecter, sauvegarder, chercher et comparer
	
def detectTH():

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

	dweeps = dweepy.get_dweets_for('Assistant')
	for dweep in dweeps:
		created = dweep['created']
		created_string = str(cr)
		heure = (((s.split('T'))[1]).split(':'))[0]
		minute = (((s.split('T'))[1]).split(':'))[1]
	# Fonction qui donne la temperature et humidite d'une heure,
	# stockees en forme de dweet.
	# Donnees : heure : float
	# Resultat : Tuple (temperature,humidite)
	pass

def compareJourTH(temp1, hum1):

	# Fonction qui compare la temperature et l'humidite actuelles avec les parametres
	# de le jour dernier a la meme heure
	# Donnees : temp1, hum1: parametres environnementaux actuels	
	# Resultat : alert : int, code de alerte ( pour identifier apres le texte propre 
	#                                         pour l'avis)
	 
def compareHeureTH(temp1, hum1, tempd, humd):


	# Fonction qui compare deux ensembles de (temperature, humidite) 
	# et "decide" si une alerte doit etre donnee.
	# Donnees : temp1, hum1: parametres environnementaux actuels				
	# Resultat : alert : (int, int) , code de alerte ( pour identifier apres le texte propre 
	#                                         a envoyer par mail)

	
	DonneeDerniereHeure = dweepy.get_latest_dweet_for('Assistant')
	diffTemp = temp1 - DonneeDerniereHeure[0]['content']['Temperature']
	diffHum = hum1 - DonneeDerniereHeure[0]['content']['Humidite']
	
	return (diffTemp, diffHum)




	pass

if __name__ == '__main__':
	[t, h] = detectTH()
	print(t,h)
	saveTH(11,22)
