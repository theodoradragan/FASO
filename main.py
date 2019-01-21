# Ce programme va avoir la boucle while infinie

from mail import *
from manageData import *
from sendAdvice import *
from sendAlert import *
from affichage import *
from datetime import datetime # pour obtenir l'heure courant
from grovepi import *

period = 5 # 5 secondes entre les detections
button = 8
tempmoy = 17

def readFromConfig():
	tempmoy = 17 # should be altered by config

def main():
	dweepy.dweet_for('Assistant', {'Temperature' : 25, 'Humidite' : 25})
	# ^ Pour avoir des donnees en 'Assistant'
	x = 0
	inDemo = True # true pour le demo
	while True:

		# Turn off led if the button is pressed

		if digitalRead(button) == 1 :
			turnOffLed()

		[tempExt, humExt] = detectTHExterieure()
		[tempInt, humInt] = detectTHInterieure()
		
		printTH(tempInt, humInt)

		print(tempInt, humInt)
		print(tempExt, humExt)
		
		
		# (tempdh, humdh) = loadTH(heure) # pour les alertes, on compare avec le jour dernier

		if userAtDoor():
			advice = getAdvice(tempExt, humExt)
			playAdvice(advice)
			print(advice)

		# if x % 5 == 0 : # pour simuler une sortie periodique de l'user
		# 	advice = getAdvice(tempExt, humExt)
		# 	playAdvice(advice)
		# 	print(advice)

		# advice = getAdvice(tempExt, humExt) # debug , will delete
		# print(advice) # debug , will delete
		# playAdvice(advice) # debug , will delete
		
		# now = datetime.now()
		# heure = now.hour
		# minute = now.minute
		# print("Heure")
		# print(heure)
		# print("Minute")
		# print(minute)
		# if (minute == 0):
			

		# Turn off led if the button is pressed

		if digitalRead(button) == 1 :
			turnOffLed()

  #   	except IOError:
  #       	print ("Error")

		x = x + 1
		if x >= 720 or inDemo : # would be 360 for each hour, will make 18 for demo / testing purposes
			setAlert(tempInt, humInt, tempmoy, tempExt)
			inDemo = False
			x = x % 720
		
		time.sleep(period)

if __name__ == '__main__':
	main()
