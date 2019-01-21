import dweepy

# Ca sera une bibliotheque pour gerer les actions mail en regardant les alertes

globalEmail = "theoa.dragan@yahoo.com"
tempmoy = 17

def setRecipient(email):
	# Fonction pour etablir le mail pour les alertes
	# Donnee : nouveau mail de l'utilisateur, string
	# Resultat : -
	globalEmail = email

def setAlert(diffT, temp, hum, tempmoy, tempext):

	alertResponse = getAlertText(diffT, temp, hum, tempmoy, tempext)
	alertString = "if(dweet.Temperature >" + tempmoy +" 17) return ' " + alertResponse + "';"
	dweepy.set_alert(
		'JarvisThing',
		[globalEmail],
		alertString,
		'this-is-a-key',
	)
