# -*- coding: utf-8 -*-

# Class / bibliotheque pour envoyer les avis
import os # pour executer des commands en terminal linux 
# on utilisera le grove.py pour verifier le passage de l'user a la porte
from grovepi import *
# et espeak pour text-to-speech

cloVetements = {
	# sous-vetements
	0.03 : "lingerie",
	0.06 : "half-leggings",
	0.1 : "leggings",

	# blouses in general
	0.06 : "sleeveless shirt",
	0.09 : "T-shirt",
	0.12 : "shirt with long sleeves",
	0.30 : "flannel shirt with long sleeves",
	0.34 : "long sleeves with turtlenech blouse",

	# pantalons en general
	0.06 : "shorts",
	0.20 : "light trousers",
	0.25 : "normal trousers",
	0.28 : "flannel trousers",
	0.28 : "overalls",

	# sweaters
	0.12 : "sleeveless vest",
	0.25 : "light summer jacket",
	0.35 : "jacket",
	0.55 : "down jacket",
	0.60 : "coat",

	# pour les pieds :
	0.02 : "socks",
	0.03 : "slippers",
	0.02 : "sandals",
	0.02 : "sportive shoes",
	0.02 : "this-soled shoes",
	0.04 : "thick-soled shoes",
	0.05 : "thick ankle socks",
	0.05 : "boots",
	0.10 : "thick long socks",

	# accessories : 
	0.05 : "cap",
}

humidexToAdvice = {
	29 : "Peu de gens sont incommodés.",
	34 : "Sensation de malaise plus ou moins grande.",
	39 : "Sensation de malaise assez grande. Prudence. Ralentir certaines activités en plein air.",
	45 : "Sensation de malaise généralisée.  Danger. Eviter les efforts.",
	53 : "Danger extrême.  Arrêt de travail dans de nombreux domaines.",
	100 : "Coup de chaleur imminent (danger de mort)."
}

# Lookup table for humidity index
humidex = {
	# temperature : [(humidity, humidex)]
	21 : [(40, 21), (45, 22)],
	# 22 :
	# 23 : 
	# 24 : 
}
	


ultrasonic_ranger = 4 # Digital entrance on board (D7)

def calculateCloNeeded(tempExt):
	# Fonction qui calcule le clo indice pour savoir combien des vetements
	# on a besoin.
	# Donnees : temperature Exterieure Courante
	# Resultat : le clo indice, truncated avec 2 decimales (1,1234 devient 1,12 pour mieux calculer)
	# On utilise le fait que, selon des recherches, 1 clo est necessaire pour se sentir
	# confortable dans 21 degres Celcius

	clo = tempExt / 21
	roundedClo = round(clo, 2)
	return roundedClo

def getAdvice(tempExt, humExt):
	# Fonction qui cherche dans les textes predefinis le
	# texte propre pour la temperature exterieure courante
	# Donnees : tempExt : float, la temperature exterieure
	# Resultat : advice : string, l'avis pour cettes conditions

	advice = "Bonne journee !"
	humIdxValue = 0

	for (hum, humIdx) in humidex[tempExt]:
		if hum < humExt:
			humIdxValue = humExt

	for adv in humidexToAdvice :
		print()

	return advice


def playAdvice(advice):
	# Fonction qui prend le conseil sous forme de texte et le 
	# diffuse via les haut-parleurs.
	# Donnees : codeAdvice : int, type of difference
	# Resultat : advice : string

	# cette commande est pour assurer que l'output de son est analog
	# c'est a dire les haut-parleurs.
	command = "amixer cset numid=3 1"
	os.system(command)

	command = 'espeak -vfr ' + advice
	os.system(command)

def getProximity():
	# Fonction qui prendre la distance mesure par l'ultrason.
	# Donnees : -
	# Resultat : distance
	return ultrasonicRead(ultrasonic_ranger)

def userAtDoor():
	# Fonction qui detecte si l'user est en train de partir de chez lui.
	# Donnees : codeAdvice : int, type of difference
	# Resultat : boolean, true if user is at the door

	distance = getProximity()
	print("Distance is")
	print(distance)
	if distance < 5:
		return True
		
	return False


