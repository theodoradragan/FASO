# On allons utiliser driveri2c pour allumer le LED
import time
from grovepi import *

led = 2 #D2 port pour LED

# Look up table for humidity, based on lower value of the range

def turnOnLED():
	# Fonction pour allumer le led
	pinMode(led,"OUTPUT")
	time.sleep(1)

	while True:
		try:
			digitalWrite(led,1)
			print("LED ON !")
			time.sleep(1)

			digitalWrite(led,0)
			print("LED OFF !")
			time.sleep(1)

		except KeyboardInterrupt:
			digitalWrite(led, 0)
			break

		except IOError:
			print("Error")

def getAlertText(diffT, codeDiffH): #deux codes : le premier pour la temperature, le deuxieme pour l'humidite
	strt = "Soyez attentif! Votre temperature est "
	strt = strt + abs(diffTemp)

	if diffT > 0:
		strt = strt + "plus"
	else
		strt = strt + "moins"
	strt = strt + "que l'heure precedente.\n"

	if diffT > 0:
		if diffT < 2:
			strt  = strt + "Consommation d'energie non necessaire.\n"
		elif diffT< 4:
			strt = strt + "Alerte pour difference 2-4"
		elif diffT< 6:
			strt = strt + "Alerte pour difference 4-6"
		elif diffT< 8:
			strt = strt + "Alerte pour difference 6-8"
		else:
			strt = strt + "Alerte pour difference >8"

	else:
		if diffT > -2:
			strt  = strt + "C'est plus froid que recommendable.\n"
		elif diffT > -4:
			strt = strt + "Alerte pour difference -2 - -4"
		elif diffT > -6:
			strt = strt + "Alerte pour difference -4--6"
		elif diffT >- 8:
			strt = strt + "Alerte pour difference -6--8"
		else:
			strt = strt + "Alerte pour difference >-8"

def sendMailAlert(diffT, diffH):
	getAlertText(diffT, diffH)
	mail.sendMail()




if __name__=='__main__':
	turnOnLED()
