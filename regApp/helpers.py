from django.core.mail import send_mail
import uuid

def sendMail(subject, recipient, message):
	'''recipient list in [rec_list]'''
	send_mail(subject, message, 'members@npc.ge', [recipient])

def generateUID():
	return uuid.uuid4()

def getConfirmationLink(email, uid):
	Email = str(email).replace('@', 'atsymbol') + '/'
	UID = str(uid)
	link = 'http://www.npc.ge/emailconfirmation/'
	link += Email + UID
	return link