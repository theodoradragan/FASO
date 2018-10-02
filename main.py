# Ce programme va avoir la boucle while infinie

from mail import *
from manageData import *
from sendAdvice import *
from sendAlert import *
from affichage import *

def readFromConfig():
	# Reads running settings from the config file
	pass

def main():
	x = 0
	while True:
		[temp, hum] = detectTH()
		#print(temp)
		#print(hum)
		printTH(temp, hum)
		x = x + 1
		if x == 20:
			break

if __name__ == '__main__':
	main()
