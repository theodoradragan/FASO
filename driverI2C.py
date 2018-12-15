#from time import *
import time
from grovepi import *

bus = smbus.SMBus(1)  # pour I2C-1 (0 pour I2C-0)

# Indiquez ici les deux adresses de l'ecran LCD
# celle pour les couleurs du fond d'ecran 
# et celle pour afficher des caracteres
DISPLAY_RGB_ADDR = 0x62
DISPLAY_TEXT_ADDR = 0x3e


# Decommentez et completez le code de la fonction permettant de choisir
# la couleur du fond d'ecran, n'oubliez pas d'initialiser l'ecran
def setRGB(rouge,vert,bleu):
	# rouge, vert et bleu sont les composantes de la couleur demandee
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x00,0x00)
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x01,0x00)
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x08,0xaa)
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x04,rouge)
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x03,vert)
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x02,bleu)
	print("Couleur ecran changee")

# Envoie  a l'ecran une commande concerant l'affichage des caracteres
# (cette fonction vous est donnes gratuitement si vous
# lutilisez dans la fonction suivante, sinon donnez 2000
# a la banque et allez directement en prison :)
def textCmd(cmd):
	bus.write_byte_data(DISPLAY_TEXT_ADDR,0x80,cmd)
	
# Completez le code de la fonction permettant d'ecrire le texte recu en parametre
# Si le texte contient un \n ou plus de 16 caracteres pensez a gerer
# le retour a la ligne
def setText(texte):
	textCmd(0x01)
	time.sleep(0.05)
	textCmd(0x08 | 0x04)	

	#textCmd(0x0F)
	textCmd(0x28) #pour avoir 2 lignes
	time.sleep(0.05)
	count = 0
	row = 0

	while len(texte) < 32:
		texte+= ' '

	for c in texte:
		if c == '\n' or count == 16:
			count = 0
			row +=1
			if row == 2:
				break
			textCmd(0xc0)
			if c == '\n':
				continue
		count += 1
		bus.write_byte_data(DISPLAY_TEXT_ADDR,0x40,ord(c))

#la fonction permet de parametrer les couleurs
def setColor(y): 
	if y=="Blanc":
		setRGB(0xFF,0xFF,0xFF)
	elif y=="Rouge":
		setRGB(0xFF,0x00,0x00)
	elif y=="Vert":
		setRGB(0x00,0xFF,0x00)
	elif y=="Bleu":
		setRGB(0x00,0x00,0xFF)
	elif y=="Violet":
		setRGB(0xFF,0x00,0xFF)
	
if __name__ == '__main__':
	print("Before")
	setColor("Rouge")
	setText("Hello")
	print("Done")
