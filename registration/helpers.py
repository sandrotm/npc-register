from django.core.mail import send_mail
import uuid

def sendMail(subject, recipient, message):
	'''recipient list in [rec_list]'''
	send_mail(subject, message, 'members@npc.ge', [recipient])

def generateUID():
	return uuid.uuid4()