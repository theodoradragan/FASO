import dweepy
import Adafruit_DHT

# Ca sera une bibliotheque pour gerer les temperatures et humidites : 
# detecter, sauvegarder, chercher et comparer

def detectTH():

	# Fonction qui retourne la temperature et l'humidite
	# Donnees : -
	# Resultat : Touple (humidite, temperature)


	sensor = Adafruit_DHT.DHT11
	#pin = 23
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	return (temperature,humidity)

def saveTH(temperature,humidite):
	
	# Fonction qui crée et envoie un tweet avec la température 
	# et l'humidité actuelles de cette heure.
	# Donnees : temperature : float, humidite : float
	# Resultat : -

def loadTH(heure):

	# Fonction qui donne la temperature et humidite d'une heure,
	# stockees en forme de dweet.
	# Donnees : heure : float
	# Resultat : Tuple (temperature,humidite)

def compareJourTH(temp1, hum1):

	# Fonction qui compare la température et l'humidité actuelles avec les paramètres
	# de le jour dernier a la meme heure
	# Donnees : temp1, hum1: paramètres environnementaux actuels	
	# Resultat : alert : int, code de alerte ( pour identifier apres le texte propre 
	#                                         pour l'avis)

def compareHeureTH(temp1, hum1):

	# Fonction qui compare deux ensembles de (température, humidité) 
	# et "décide" si une alerte doit être donnée.
	# Donnees : temp1, hum1: paramètres environnementaux actuels				
	# Resultat : alert : int, code de alerte ( pour identifier apres le texte propre 
	#                                         a envoyer par mail)


