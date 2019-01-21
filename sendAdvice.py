# -*- coding: utf-8 -*-

# Class / bibliotheque pour envoyer les avis
import os # pour executer des commands en terminal linux 
# on utilisera le grove.py pour verifier le passage de l'user a la porte
from grovepi import *
# et espeak pour text-to-speech

ultrasonic_ranger = 7 # Digital entrance on board (D7)

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

humidexToAdvice = [
	# (limite superieur pour cet avis, avis)
	(29, "Peu de gens sont incommodés."),
	(34, "Une Sensation de malaise plus ou moins grande."),
	(39, "Une Sensation de malaise assez grande. Prudence. Ralentir certaines activités en plein air."),
	(45, "Une Sensation de malaise généralisée.  Danger. Eviter les efforts."),
	(53, "Il y a un danger extrême.  Il faut arrêter toutes les activités"),
	(100, "Vous risquez un coup de chaleur imminent (danger de mort)."),
]

# Lookup table for humidity index
humidex = {
	# temperature : [(humidity, humidex)]
	# on a mis humidex 20 pour les valeurs non trouvees dans la recherche, seulement pour avoir tous les cas possibles
	16 : [(20, 20), (25, 21), (30, 21), (35, 20), (40, 20), (45, 21), (50, 22), (55, 23), (60, 24), (65, 24), (70, 25), (75, 26), (80, 26), (85, 27), (90, 28), (95, 28), (100, 29)],
	17 : [(20, 20), (25, 21), (30, 21), (35, 20), (40, 20), (45, 21), (50, 22), (55, 23), (60, 24), (65, 25), (70, 26), (75, 27), (80, 28), (85, 29), (90, 30), (95, 31), (100, 31)],
	18 : [(20, 20), (25, 22), (30, 21), (35, 20), (40, 20), (45, 21), (50, 22), (55, 24), (60, 25), (65, 26), (70, 27), (75, 28), (80, 29), (85, 30), (90, 31), (95, 32), (100, 32)],
	19 : [(20, 20), (25, 22), (30, 22), (35, 21), (40, 21), (45, 22), (50, 23), (55, 25), (60, 26), (65, 27), (70, 28), (75, 29), (80, 30), (85, 31), (90, 32), (95, 33), (100, 34)],
	20 : [(20, 20), (25, 23), (30, 22), (35, 21), (40, 21), (45, 22), (50, 24), (55, 26), (60, 27), (65, 28), (70, 29), (75, 30), (80, 31), (85, 32), (90, 33), (95, 34), (100, 35)],
	21 : [(20, 21), (25, 24), (30, 22), (35, 21), (40, 21), (45, 22), (50, 25), (55, 27), (60, 28), (65, 29), (70, 30), (75, 31), (80, 32), (85, 33), (90, 34), (95, 35), (100, 36)],
	22 : [(20, 22), (25, 25), (30, 23), (35, 22), (40, 22), (45, 23), (50, 25), (55, 28), (60, 29), (65, 30), (70, 31), (75, 32), (80, 33), (85, 34), (90, 35), (95, 36), (100, 37)],
	23 : [(20, 23), (25, 25), (30, 24), (35, 23), (40, 24), (45, 25), (50, 26), (55, 29), (60, 30), (65, 31), (70, 32), (75, 33), (80, 34), (85, 35), (90, 36), (95, 37), (100, 38)],
	24 : [(20, 24), (25, 26), (30, 25), (35, 24), (40, 25), (45, 26), (50, 27), (55, 30), (60, 31), (65, 32), (70, 33), (75, 34), (80, 35), (85, 36), (90, 37), (95, 38), (100, 39)],
	25 : [(20, 24), (25, 27), (30, 25), (35, 25), (40, 26), (45, 27), (50, 29), (55, 31), (60, 32), (65, 33), (70, 34), (75, 35), (80, 36), (85, 37), (90, 38), (95, 39), (100, 40)],
	26 : [(20, 26), (25, 28), (30, 26), (35, 27), (40, 28), (45, 29), (50, 30), (55, 32), (60, 33), (65, 34), (70, 35), (75, 36), (80, 37), (85, 38), (90, 39), (95, 40), (100, 41)],
	27 : [(20, 27), (25, 29), (30, 27), (35, 28), (40, 29), (45, 30), (50, 31), (55, 33), (60, 34), (65, 35), (70, 36), (75, 37), (80, 38), (85, 39), (90, 40), (95, 41), (100, 42)],
	28 : [(20, 28), (25, 30), (30, 28), (35, 30), (40, 31), (45, 31), (50, 31), (55, 33), (60, 35), (65, 36), (70, 37), (75, 38), (80, 39), (85, 40), (90, 41), (95, 42), (100, 43)],
	29 : [(20, 31), (25, 31), (30, 29), (35, 31), (40, 32), (45, 33), (50, 32), (55, 34), (60, 36), (65, 37), (70, 38), (75, 39), (80, 40), (85, 41), (90, 42), (95, 43), (100, 44)],
	30 : [(20, 32), (25, 32), (30, 30), (35, 32), (40, 34), (45, 36), (50, 34), (55, 35), (60, 37), (65, 38), (70, 39), (75, 40), (80, 41), (85, 42), (90, 43), (95, 44), (100, 45)],
	31 : [(20, 32), (25, 33), (30, 31), (35, 34), (40, 35), (45, 36), (50, 36), (55, 36), (60, 38), (65, 39), (70, 40), (75, 41), (80, 42), (85, 43), (90, 44), (95, 45), (100, 46)],
	32 : [(20, 32), (25, 33), (30, 33), (35, 35), (40, 37), (45, 38), (50, 37), (55, 38), (60, 39), (65, 40), (70, 41), (75, 42), (80, 43), (85, 44), (90, 45), (95, 46), (100, 47)],
	33 : [(20, 33), (25, 33), (30, 34), (35, 37), (40, 38), (45, 39), (50, 39), (55, 39), (60, 41), (65, 42), (70, 43), (75, 44), (80, 45), (85, 46), (90, 47), (95, 48), (100, 48)],
	34 : [(20, 34), (25, 34), (30, 35), (35, 39), (40, 40), (45, 41), (50, 43), (55, 41), (60, 43), (65, 44), (70, 45), (75, 46), (80, 47), (85, 47), (90, 48), (95, 49), (100, 50)],
	35 : [(20, 35), (25, 35), (30, 37), (35, 40), (40, 42), (45, 43), (50, 45), (55, 45), (60, 44), (65, 45), (70, 46), (75, 47), (80, 48), (85, 48), (90, 49), (95, 50), (100, 51)],
	36 : [(20, 36), (25, 36), (30, 40), (35, 42), (40, 43), (45, 45), (50, 46), (55, 47), (60, 47), (65, 48), (70, 49), (75, 50), (80, 49), (85, 49), (90, 50), (95, 51), (100, 53)],
	37 : [(20, 37), (25, 37), (30, 42), (35, 43), (40, 45), (45, 45), (50, 47), (55, 49), (60, 49), (65, 50), (70, 51), (75, 52), (80, 53), (85, 53), (90, 55), (95, 55), (100, 54)],
	38 : [(20, 38), (25, 38), (30, 43), (35, 45), (40, 47), (45, 48), (50, 49), (55, 50), (60, 51), (65, 52), (70, 53), (75, 54), (80, 55), (85, 56), (90, 57), (95, 57), (100, 57)],
	39 : [(20, 40), (25, 39), (30, 45), (35, 47), (40, 49), (45, 51), (50, 50), (55, 52), (60, 53), (65, 54), (70, 54), (75, 55), (80, 26), (85, 57), (90, 58), (95, 59), (100, 60)],
	40 : [(20, 41), (25, 41), (30, 47), (35, 49), (40, 51), (45, 52), (50, 51), (55, 53), (60, 53), (65, 55), (70, 56), (75, 57), (80, 58), (85, 58), (90, 59), (95, 60), (100, 61)],
	41 : [(20, 43), (25, 43), (30, 49), (35, 50), (40, 52), (45, 57), (50, 53), (55, 55), (60, 54), (65, 55), (70, 57), (75, 58), (80, 59), (85, 60), (90, 61), (95, 62), (100, 63)],
}

def calculateCloNeeded(tempExt):
	# Fonction qui calcule le clo indice pour savoir combien des vetements
	# on a besoin.
	# Donnees : temperature Exterieure Courante
	# Resultat : le clo indice, truncated avec 2 decimales (1,1234 devient 1,12 pour mieux calculer)
	# On utilise le fait que, selon des recherches, 1 clo est necessaire pour se sentir
	# confortable dans 21 degres Celsius

	clo = tempExt / 21
	roundedClo = round(clo, 2)
	return roundedClo

def getAdvice(tempExt, humExt):
	# Fonction qui cherche dans les textes predefinis le
	# texte propre pour la temperature exterieure courante
	# Donnees : tempExt : float, la temperature exterieure
	# Resultat : advice : string, l'avis pour cettes conditions

	advice = "La temperature exterieure est " + str(int(tempExt)) + " et l'humidite exterieure est " + str(int(humExt)) + " %, dans ces conditions"
	humIdxValue = 0
	tempExtEntier = int(tempExt)

	for (hum, humIdx) in humidex[tempExtEntier]:
		if hum < humExt:
			humIdxValue = humExt

	i = 0
	while i < len(humidexToAdvice):
		(limiteSup, avis) = humidexToAdvice[i]
		if limiteSup >= humIdxValue:
			# We found the proper advice, we can stop searching for it
			(_, adviceAfter) = humidexToAdvice[i]
			advice = advice + adviceAfter
			break
		i = i + 1
	return advice


def playAdvice(advice):
	# Fonction qui prend le conseil sous forme de texte et le 
	# diffuse via les haut-parleurs.
	# Donnees : codeAdvice : int, type of difference
	# Resultat : advice : string

	# cette commande est pour assurer que l'output de son est analog
	# c'est a dire les haut-parleurs.
	command = "amixer cset numid=3 1 >/dev/null 2>&1 "
	os.system(command)

	command = "espeak -vfr -s 150 \" " + advice + " \" >/dev/null 2>&1 "
	# print("Command is")
	# print(command)
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

	somme = 0
	for i in range(0, 7):
		distance = getProximity()
		time.sleep(0.1)
		somme = somme + distance
	distance = somme / 7

	if distance <= 10:
		return True
	
	return False