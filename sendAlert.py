# On allons utiliser driveri2c pour allumer le LED
import time
from grovepi import *

led = 2 #D2 port pour LED

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

if __name__=='__main__':
	turnOnLED()
