import dweepy
from sendAlert import *
import smtplib, ssl
# Ca sera une bibliotheque pour gerer les actions mail en regardant les alertes

# Donnes pour le mail
smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "jarvis.faso@gmail.com"
password = "FASO12345678"

globalEmail = "theoa.dragan@yahoo.com"
tempmoy = 10 # 10 for testing, just to make sure we get an alert

def setRecipient(email):
	# Fonction pour etablir le mail pour les alertes
	# Donnee : nouveau mail de l'utilisateur, string
	# Resultat : -
	globalEmail = email

def setAlert(temp, hum, tempmoy, tempext):

	message = """\
	Subject: Hi there

	""" + getAlertText(temp, hum, tempmoy, tempext)

	# Create a secure SSL context
	context = ssl.create_default_context()

	# Try to log in to server and send email
	try:
	    server = smtplib.SMTP(smtp_server,port)
	    server.ehlo() # Can be omitted
	    server.starttls() # Secure the connection
	    server.ehlo() # Can be omitted
	    server.login(sender_email, password)
	    server.sendmail(sender_email, globalEmail, message) # let's not spam while testing
	except Exception as e:
	    # Print any error messages to stdout
	    print(e)
	finally:
	    server.quit() 

	print("Dweeeeeeeeeeeeeetssssssssss")
	print(dweepy.get_dweets_for('Assistant'))

	# alertResponse = getAlertText(temp, hum, tempmoy, tempext)
	# if (alertResponse != ""):
	# 	alertString = "if(dweet.Temperature > " + str(tempmoy) +" ) return ' " + alertResponse + "';"
	# 	dweepy.set_alert(
	# 		'JarvisThing',
	# 		[globalEmail],
	# 		alertString,
	# 		'this-is-a-key',
	# 	)
	pass