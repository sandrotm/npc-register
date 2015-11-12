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
	# Email = str(email).replace('@', 'at_symbol') + '/'
	# Email = Email.replace('.', 'dot_symbol')
	try:
		email = processMail(email)
		print(email)
		print(uid)
		UID = str(uid)
		link = 'http://www.npc.ge/register/confirm/'
		link += email + '/' + UID
		print(link)
		return link
	except Exception as ge:
		print('from gcl ' + str(ge))

def processMail(mail, extract = False):
	chars = ['!', '@', '#', '$', '%', 
		'^', '&', '*', '(', ')',
		'-', '+', '=', '?',
		'.', ',', '[', ']', ':',
		';', '/', '{', '}']
	charAlts = ['exclamation_symbol', 'at_symbol', 'hash_symbol',
		'dollar_symbol', 'percent_symbol', 'power_symbol', 
		'and_symbol', 'asterisk_symbol', 'brackL_symbol', 
		'brackR_symbol', 'dash_symbol', 
		'plus_symbol', 'equal_symbol', 'question_symbol',
		'dot_symbol', 'comma_symbol', 'sqbrL_symbol', 
		'sqbrR_symbol', 'column_symbol', 'smcolumn_symbol', 
		'slash_symbol', 'rndL_symbol', 'rndR_symbol']
	
	#when mail is sending
	if not extract:
		for i in range(0, len(chars)):
			if chars[i] in mail:
				mail = mail.replace(chars[i], charAlts[i])
	else: #when link is being confirmed
		for i in range(0, len(chars)):
			if charAlts[i] in mail:
				mail = mail.replace(charAlts[i], chars[i])

	return mail
