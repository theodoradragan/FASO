# Ce programme va avoir la boucle while infinie

from mail import *
from manageData import *
from sendAdvice import *
from sendAlert import *
from affichage import *
from datetime import datetime # pour obtenir l'heure courant

period = 10 # 10 secondes entre les detections
button = 8
tempmoy = 17

def readFromConfig():
	tempmoy = 17 # should be altered by config

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
			#playAdvice(getAdvice(tempInt, humInt, tempExt, humExt)) # <-- normal behaviour, if sensor wouldn't have been broken

		if x % 5 == 0 : # pour simuler une sortie periodique de l'user
			playAdvice(getAdvice(tempInt, humInt, tempExt, humExt))
		
		setAlert(tempInt, humInt, tempmoy, tempExt)

		# Turn off led if the button is pressed
		try:
        	if (grovepi.digitalRead(button)):
        		turnOffLed()

    	except IOError:
        	print ("Error")

		x = x + 1
		if x == 2000:
			break
		saveTH(tempInt, humInt)
		time.sleep(period)

if __name__ == '__main__':
	main()
