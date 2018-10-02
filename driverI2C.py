# coding: utf-8
import smbus

bus = smbus.SMBus(1)  # pour I2C-1 (0 pour I2C-0)

# Indiquez ici les deux adresses de l'ecran LCD
# celle pour les couleurs du fond d'ecran 
# et celle pour afficher des caracteres
DISPLAY_RGB_ADDR = 0x62
DISPLAY_TEXT_ADDR = 0x3e


# Décommentez et completez le code de la fonction permettant de choisir
# la couleur du fond d'ecran, n'oubliez pas d'initialiser l'ecran
def setRGB(rouge,vert,bleu):
	# rouge, vert et bleu sont les composantes de la couleur demandée
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x00,0x00)
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x01,0x00)
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x04,rouge) # <--- ?
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x03,vert) # <--- ?
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x02,bleu) # <--- ?
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x08,0xAA)
	print("Couleur écran changée")

# Envoie  a l'ecran une commande concerant l'affichage des caracteres
# (cette fonction vous est donnes gratuitement si vous
# l'utilisez dans la fonction suivante, sinon donnez 2000€
# a la banque et allez directement en prison :)
def textCmd(cmd):
	bus.write_byte_data(DISPLAY_TEXT_ADDR,0x80,cmd)
	
# Completez le code de la fonction permettant d'ecrire le texte recu en parametre
# Si le texte contient un \n ou plus de 16 caracteres pensez a gerer
# le retour a la ligne
def setText(texte):
	textCmd(0x01)
	textCmd(0x0F)
	textCmd(0x38) #pour avoir 2 lignes
	for i in range (0,len(texte)-1) :
		c = texte[i]
		if (c=='\n' or i==17):  # si on depasse 16 caracteres
			textCmd(0xc0)
		if (c=='\n') : 
			i=i+1
			c=texte[i]
		bus.write_byte_data(DISPLAY_TEXT_ADDR,0x40,0x10)#pour afficher c à l'écran
	print ("texte ecrit")

#la fonction permet de paramétrer les couleurs
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
