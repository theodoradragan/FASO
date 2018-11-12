# Ce programme va avoir la boucle while infinie

from mail import *
from manageData import *
from sendAdvice import *
from sendAlert import *
from affichage import *
from datetime import datetime # pour obtenir l'heure courant

period = 300 # 5 minutes entre les detections, pour tester.
	 # en secondes

def readFromConfig():
	# Reads running settings from the config file
	pass

def main():
	x = 0
	while True:
		[temp, hum] = detectTH()
		
		printTH(temp, hum)
		
		now = datetime.now()
		heure = now.hour
		(tempdh, humdh) = loadTH(heure) # pour les alertes, on compare avec le jour dernier
		codeAlerte = compareJourTH(temp, hum, tempdh, humdh)
 		


		x = x + 1
		if x == 20:
			break
		saveTH(temp, hum)
		time.sleep(period)

if __name__ == '__main__':
	main()
