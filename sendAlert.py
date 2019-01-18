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

def getAlertText(diffT, temp, hum, tempmoy, tempext): 

	# Deux parametres indiquant la difference par rapport à l'heure precedente : 
	# Le premier pour la difference de temperature, le deuxieme pour la différence d'humidite
	# Les quatres autres parametres son la temp actuelle ,l'hum actuelle et la temp moyenne definit dans le fichier config et la temp exterieure
	strt = "Soyez attentif! Votre temperature est de"
	strt = strt + abs(diffT) + "degres"
	
	if diffT > 0:
		strt = strt + "superieur"
	else
		strt = strt + "inferieur"
	strt = strt + " à l'heure precedente.\n"

	if temp > tempmoy: # cas augmentation temperature
		strt = strt + "La temperature de votre habitat est plus chaude que la temperature moyenne que vous avez definit. \n"
		if temp > tempext: #on est en hiver
			if diffT < 2 && diffT > 0:
				strt  = strt + "Consommation d'energie non necessaire.\n"
			elif diffT < 4 && difT >= 2:
				strt = strt + "Pensez a eteindre le chauffage ou a diminuer le termostat. \n"
			elif diffT < 6 && difT >= 4:
				strt = strt + "Pensez a eteindre le chauffage ou a diminuer le termostat. \n"
			elif diffT < 8 && difT >= 6:
				strt = strt + "Si vous n'avez pas prévu cette hausse de temperature. Verifiez ce qui a pu causer une hausse si importante en une heure. \n"
			else:
				strt = strt + "Cet assistant ne permet pas de vous prevenir en cas d'incendie a votre domicile mais nous vous conseillons de verifier ce qui a pu entrainer cette hausse de temperature. \n"
			strt = strt + "si ces informations ne vous semble pas pertinente verifier que la temperature moyenne definit via l'application mobile est celle que vous souhaitez dans votre habitat. \n"
		else: # on est en ete
			if diffT < 2:
				strt  = strt + "Cette hausse peut provenir d'appareils electroniques ou de fenetres laissees ouvertes.\n"
			elif diffT < 4 && difT >= 2:
				strt = strt + "Cette hausse peut provenir de fenetres ouvertes.\n"
			elif diffT < 6 && difT >= 4
				strt = strt + "Cette hausse peut provenir de fenetres ouvertes, verifiez la cause de cette hausse.\n"
			elif diffT < 8 && difT >= 6:
				strt = strt + "Si vous n'avez pas prevu cette hausse de temperature. Verifiez ce qui a pu causer une hausse si importante en une heure. \n"
			else:
				strt = strt + "Cet assistant ne permet pas de vous prevenir en cas d'incendie a votre domicile mais nous vous conseillons de verifier ce qui a pu entrainer cette hausse de temperature. \n"
			strt = strt + "si ces informations ne vous semble pas pertinente verifier que la temperature moyenne definit via l'application mobile est celle que vous souhaitez dans votre habitat. \n"
	
	else:
		if temp > tempext: # on est en hiver
			strt = strt + "La temperature de votre habitat est plus froide que la temperature moyenne que vous avez definit. \n"
			if diffT > -2 && diff < 0:
				strt  = strt + "Penser a rechauffer votre habitat.\n"
			elif diffT > -4 && diff <= -2:
				strt = strt + "Penser a rechauffer votre habitat et verifiez que vous n'avez pas laisse les fenetres ouvertes.\n"
			elif diffT > -6 && diff <= -4:
				strt = strt + "Penser a rechauffer votre habitat et verifiez que vous n'avez pas laisse les fenetres ouvertes ou toutes autres causes provoquant cette baisse. \n"
			elif diffT >- 8 && diff <= -6:
				strt = strt + "Si vous n'avez pas prevu cette baisse de temperature. Verifiez ce qui a pu le provoquer. \n"
			else:
				strt = strt + "Cet assistant ne permet pas de vous prévenir en cas d'incident dans votre domicile mais nous vous conseillons de verifier ce qui a pu entrainer cette baisse de temperature. \n"
		else: # on est en ete
			strt = strt + "La temperature de votre habitat est plus froide que la temperature moyenne que vous avez definit. \n"
			if diffT > -2 && diff < 0:
				strt  = strt + "Consommation d'energie non necessaire.\n"
			elif diffT > -4 && diff <= -2:
				strt = strt + "Pensez a eteindre votre systeme de climatisation, consomation d'energie non necessaire. \n"
			elif diffT > -6 && diff <= -4:
				strt = strt + "Pensez a eteindre votre systeme de climatisation, consomation d'energie non necessaire. \n"
			else:
				strt = strt + "Cet assistant ne permet pas de vous prévenir en cas d'incident dans votre domicile mais nous vous conseillons de verifier ce qui a pu entrainer cette baisse de temperature. \n"
			strt = strt + "si ces informations ne vous semble pas pertinente verifier que la temperature moyenne definit via l'application mobile est celle que vous souhaitez dans votre habitat. \n"
	#humidite	
	strt = strt + " votre humidite actuelle  est de " + hum + "% \n"
	
	if hum < 40:
		str = str + "Ce taux d’humidite est trop faible ce qui peut rendre votre respiration difficile, humidifiez votre habitat et pensez a bien vous hydrater. \n"

	else if hum > 55:
		str = str + "Ce taux d’humidite est trop élevé ventilez et aerez la maison et n’oubliez pas de bien vous hydrater. \n"


def sendMailAlert(diffT, diffH):
	getAlertText(diffT, diffH)
	mail.sendMail()




if __name__=='__main__':
	turnOnLED()
