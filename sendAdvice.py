# Class / bibliotheque pour envoyer les avis
import os # pour executer des commands en terminal linux 
# on utilisera le grove.py pour verifier le passage de l'user a la porte
from grovepi import *
# et espeak pour text-to-speech

ultrasonic_ranger = 4 # Digital entrance on board (D4)

def getAdvice(codeAdvice):
	# Fonction qui cherche dans les textes predefinis le
	# texte propre pour la difference de temp + humid.
	# Donnees : codeAdvice : int, type of difference
	# Resultat : advice : string
	pass

def playAdvice(advice):
	# Fonction qui prend le conseil sous forme de texte et le 
	# diffuse via les haut-parleurs.
	# Donnees : codeAdvice : int, type of difference
	# Resultat : advice : string
	pass

def getProximity():
	# Fonction qui prendre la distance mesure par l'ultrason.
	# Donnees : -
	# Resultat : distance
	return ultrasonicRead(ultrasonic_ranger)

def userAtDoor():
	# Fonction qui detecte si l'user est en train de partir de chez lui.
	# Donnees : codeAdvice : int, type of difference
	# Resultat : boolean, true if user is at the door
	pass	

def userPushedButton():
	# Fonction qui detecte si l'user demande l'avis en cette moment.
	# Donnees : - 
	# Resultat : pushed : boolean, true si l'user a appuye sur le bouton
	pass



