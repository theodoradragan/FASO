# Ce programme va avoir la boucle while infinie

from mail import *
from manageData import *
from sendAdvice import *
from sendAlert import *
from affichage import *
from datetime import datetime # pour obtenir l'heure courant
from grovepi import *
import json

period = 5 # 5 secondes entre les detections
button = 8
tempmoy = 17

def readFromConfig(fileName):
	with open(fileName) as f:
		data = json.load(f)
		return (data["Temperature moyenne"], data["Email"])

def main():
	x = 0
	(tempmoy, email) = readFromConfig("/home/pi/FASO/config.json")
	inDemo = True # true pour le demo, pour avoir une alerte a montrer
	while True:

		# Turn off led if the button is pressed

		if digitalRead(button) == 1 :
			turnOffLed()

		# On detectes les temperatures
		[tempExt, humExt] = detectTHExterieure()
		[tempInt, humInt] = detectTHInterieure()
		
		# On affiche les parametres interieurs sur l'ecran
		printTH(tempInt, humInt)

		# Si l'utilisateur veut entendre l'avis, on lui 'dit'
		if userAtDoor():
			advice = getAdvice(tempExt, humExt)
			playAdvice(advice)
			print(advice)	

		# Si le bouton est appuye, on enteint le LED

		if digitalRead(button) == 1 :
			turnOffLed()

		x = x + 1

		# On envoie le mail avec les alertes (si c'est le cas) chaque heure 
		if x >= 720 or inDemo : # 720 pour chaque heure si la periode est 5
			setAlert(tempInt, humInt, tempmoy, tempExt, email)
			inDemo = False
			x = x % 720
		time.sleep(period)


if __name__ == '__main__':
	main()
