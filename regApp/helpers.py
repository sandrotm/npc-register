from django.core.mail import send_mail
import uuid

def sendMail(subject, recipient, message):
	'''recipient list in [rec_list]'''
	send_mail(subject, message, 'members@npc.ge', recipient)

def generateUID():
	UID = str(uuid.uuid4())
	UID = UID.replace('-', '_')
	return UID

def getConfirmationLink(email, uid):
	Email = str(email).replace('@', 'at_symbol') + '/'
	Email = Email.replace('.', 'dot_symbol')
	UID = str(uid)
	link = 'http://www.npc.ge/temporary/confirm/'
	link += Email + UID
	return link
