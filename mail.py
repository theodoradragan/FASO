import dweepy

# Ca sera une bibliotheque pour gerer les actions mail en regardant les alertes

globalEmail = "theoa.dragan@yahoo.com"
tempmoy = 10 # 10 for testing, just to make sure we get an alert

def setRecipient(email):
	# Fonction pour etablir le mail pour les alertes
	# Donnee : nouveau mail de l'utilisateur, string
	# Resultat : -
	globalEmail = email

def setAlert(temp, hum, tempmoy, tempext):

	alertResponse = getAlertText(temp, hum, tempmoy, tempext)
	if (alertResponse != ""):
		alertString = "if(dweet.Temperature > " + tempmoy +" ) return ' " + alertResponse + "';"
		dweepy.set_alert(
			'JarvisThing',
			[globalEmail],
			alertString,
			'this-is-a-key',
		)
