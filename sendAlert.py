# -*- coding: utf-8 -*-

# On allons utiliser driveri2c pour allumer le LED
import time
from grovepi import *

led = 2 # D2 port pour LED

def turnOnLED():
	# Fonction pour allumer le 
	pinMode(led,"OUTPUT")
	time.sleep(1)

	try:
		digitalWrite(led,1)
		print("LED ON !")
		time.sleep(1)

	except KeyboardInterrupt:
		digitalWrite(led, 0)

	except IOError:
		print("Error")

def turnOffLed():

	pinMode(led,"OUTPUT")
	try:
		digitalWrite(led,0)
		print("LED OFF !")

	except KeyboardInterrupt:
			digitalWrite(led, 0)

	except IOError:
			print("Error")

def getAlertText(temp, hum, tempmoy, tempext):
	# Fonction qui cree le texte a envoyer a l'utilisateur
	# Les quatres parametres son la temp actuelle ,l'hum actuelle et la temp moyenne definit dans le fichier config et la temp exterieure
	
	if(temp == tempmoy):
		return ""

	diffT = temp - tempmoy	
	print("diffT is:")
	print(diffT)
	strt = ""


	if temp > tempmoy: # cas augmentation temperature
		strt = strt + "La temperature de votre habitat est plus chaude que la temperature moyenne que vous avez definit. \n"
		if temp > tempext: #on est en hiver
			
			if (diffT < 2 and diffT > 0):
				strt  = strt + "Consommation d'energie non necessaire.\n"
			elif (diffT < 4 and diffT >= 2):
				strt = strt + "Pensez a eteindre le chauffage ou a diminuer le termostat. \n"
			elif (diffT < 6 and diffT >= 4):
				strt = strt + "Pensez a eteindre le chauffage ou a diminuer le termostat. \n"
			elif (diffT < 8 and diffT >= 6):
				strt = strt + "Si vous n'avez pas prévu cette hausse de temperature, verifiez ce qui a pu causer une hausse si importante en une heure. \n"
			else:
				strt = strt + "Cet assistant ne permet pas de vous prevenir en cas d'incendie a votre domicile mais nous vous conseillons de verifier ce qui a pu entrainer cette hausse de temperature. \n"
			strt = strt + "si ces informations ne vous semble pas pertinente verifier que la temperature moyenne definit via l'application mobile est celle que vous souhaitez dans votre habitat. \n"
		else: # on est en ete
			if diffT < 2:
				strt  = strt + "Cette hausse peut provenir d'appareils electroniques ou de fenetres laissees ouvertes.\n"
			elif (diffT < 4 and diffT >= 2):
				strt = strt + "Cette hausse peut provenir de fenetres ouvertes.\n"
			elif (diffT < 6 and diffT >= 4):
				strt = strt + "Cette hausse peut provenir de fenetres ouvertes, verifiez la cause de cette hausse.\n"
			elif (diffT < 8 and diffT >= 6):
				strt = strt + "Si vous n'avez pas prevu cette hausse de temperature. Verifiez ce qui a pu causer une hausse si importante en une heure. \n"
			else:
				strt = strt + "Cet assistant ne permet pas de vous prevenir en cas d'incendie a votre domicile mais nous vous conseillons de verifier ce qui a pu entrainer cette hausse de temperature. \n"
			strt = strt + "si ces informations ne vous semble pas pertinente verifier que la temperature moyenne definit via l'application mobile est celle que vous souhaitez dans votre habitat. \n"
	
	else:
		if temp > tempext: # on est en hiver
			strt = strt + "La temperature de votre habitat est plus froide que la temperature moyenne que vous avez definit. \n"
			if diffT > -2 and diff < 0:
				strt  = strt + "Penser a rechauffer votre habitat.\n"
			elif diffT > -4 and diffT <= -2:
				strt = strt + "Penser a rechauffer votre habitat et verifiez que vous n'avez pas laisse les fenetres ouvertes.\n"
			elif diffT > -6 and diffT <= -4:
				strt = strt + "Penser a rechauffer votre habitat et verifiez que vous n'avez pas laisse les fenetres ouvertes ou toutes autres causes provoquant cette baisse. \n"
			elif diffT >- 8 and diffT <= -6:
				strt = strt + "Si vous n'avez pas prevu cette baisse de temperature. Verifiez ce qui a pu le provoquer. \n"
			else:
				strt = strt + "Cet assistant ne permet pas de vous prévenir en cas d'incident dans votre domicile mais nous vous conseillons de verifier ce qui a pu entrainer cette baisse de temperature. \n"
		else: # on est en ete
			strt = strt + "La temperature de votre habitat est plus froide que la temperature moyenne que vous avez definit. \n"
			if diffT > -2 and diffT < 0:
				strt  = strt + "Consommation d'energie non necessaire.\n"
			elif diffT > -4 and diffT <= -2:
				strt = strt + "Pensez a eteindre votre systeme de climatisation, consomation d'energie non necessaire. \n"
			elif diffT > -6 and diffT <= -4:
				strt = strt + "Pensez a eteindre votre systeme de climatisation, consomation d'energie non necessaire. \n"
			else:
				strt = strt + "Cet assistant ne permet pas de vous prévenir en cas d'incident dans votre domicile mais nous vous conseillons de verifier ce qui a pu entrainer cette baisse de temperature. \n"
			strt = strt + "si ces informations ne vous semble pas pertinente verifier que la temperature moyenne definit via l'application mobile est celle que vous souhaitez dans votre habitat. \n"
	#humidite	
	strt = strt + " votre humidite actuelle  est de " + str(hum) + "% \n"
	
	if hum < 40:
		strt = strt + "Ce taux d’humidite est trop faible ce qui peut rendre votre respiration difficile, humidifiez votre habitat et pensez a bien vous hydrater. \n"

	elif hum > 55:
		strt = strt + "Ce taux d’humidite est trop élevé! Ventilez et aerez la maison et n’oubliez pas de bien vous hydrater. \n"
	
	turnOnLED()
	return strt

if __name__=='__main__':
	turnOnLED()
