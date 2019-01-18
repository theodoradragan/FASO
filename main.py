# Ce programme va avoir la boucle while infinie

from mail import *
from manageData import *
from sendAdvice import *
from sendAlert import *
from affichage import *
from datetime import datetime # pour obtenir l'heure courant

period = 10 # 10 secondes entre les detections, pour tester.

def readFromConfig():
	# Reads running settings from the config file
	pass

def main():
	# dweepy.dweet_for('Assistant', {'Temperature' : 100, 'Humidite' : 100})
	# ^ Pour avoir des donnees en 'Assistant'
	x = 0
	while True:
		[tempExt, humExt] = detectTHExterieure()
		[tempInt, humInt] = detectTHInterieure()
		
		printTH(tempInt, humInt)

		print(tempInt, humInt)
		print(tempExt, humExt)
		
		now = datetime.now()
		heure = now.hour
		# (tempdh, humdh) = loadTH(heure) # pour les alertes, on compare avec le jour dernier
		# if tempdh is not None : 
		# 	codeAlerte = compareJourTH(temp, hum, tempdh, humdh)

		#if userAtDoor():
			#playAdvice(getAdvice(tempInt, humInt, tempExt, humExt))
			#print("Why u leavin meee?") # <-- normal behaviour, if sensor wouldn't have been broken

		if x % 5 == 0 : # pour simuler une sortie periodique de l'user
			playAdvice(getAdvice(tempInt, humInt, tempExt, humExt))
			print("Hope you heard my advice !")

		x = x + 1
		if x == 200:
			break
		# saveTH(tempInt, humInt, tempExt, humExt)
		time.sleep(period)

if __name__ == '__main__':
	main()
