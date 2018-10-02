# On utilisera le driveri2c pour l'affichage ecran
# Et il utilisera la fonction qui prend la temp + humidite courantes.
from driverI2C import *

def printTH(temp, humid):
	# Fonction qui prend les temperature et humidites plus recents enregistres et 
	# les affiche sur l'ecran
	# Donnees : temperature, humidite: float
	# Resultat : -
	t = str(temp)
	h = str(humid)
	t = "Temp: " + t + "\nHum: " + h
	print(t,h)
	setText(t)
	#setText(h)
	#setText("Bonjour")
