import dweepy

# Ca sera une bibliotheque pour gerer les actions mail en regardant les alertes

globalEmail = "theoa.dragan@yahoo.com"

def setRecipient(email):
	# Fonction pour etablir le mail pour les alertes
	# Donnee : nouveau mail de l'utilisateur, string
	# Resultat : -
	globalEmail = email

def setAlert():

	alertString = "if(dweet.alertValue > 10) return 'TEST: Greater than 10';"+
		"if(dweet.alertValue < 10) return 'TEST: Less than 10';"


	# dweepy.set_alert(
	# 	[],
	# 	alertString,
	# 	'this-is-a-key',
	# )

	print(alertString)

def sendMail(text):
	# Fonction qui envoie un mail a l'utilisateur s'il y a le cas
	# Donnee : text a envoyer a l'utilisateur, string
	# Resultat : -
	pass
