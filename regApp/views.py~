from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import MemberForm
from .models import Member
from .helpers import sendMail, generateUID, getConfirmationLink

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
	if request.method == 'POST':

		form = MemberForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			newMember = form.save()
			newMember.email_confirm = 'unconfirmed'
			newMember.member_confirm_id = str(generateUID())	
			try:
				mail_list = []
				mail_list.append(newMember.email)
				sendMail('ახალი პოლიტიკური ცენტრი', 
					mail_list,
					'თუ თქვენ შეავსეთ ახალ პოლიტიკურ ცენტრში გაწევრიანების ფორმა ' + 
					'გთხოვთ დაადასტუროთ შემდეგ მისამართზე დაჭერით ' + 
					getConfirmationLink(newMember.email, newMember.member_confirm_id))
			except Exception as ge:
				newMember.email_confirm = 'fail'
				return HttpResponse(str(ge))
			newMember.save()
			form = MemberForm()
			
			return render(request, 'regApp/index.html', {'success': 'success'})
		else:
			return render(request, 'regApp/index.html', {'form': form})

	# if a GET (or any other method) we'll create a blank form
	else:
		form = MemberForm()

	return render(request, 'regApp/index.html', {'form': form})

def confirm(request, mail, uid):
	#print(mail)
	#print(uid)
	mail = mail.replace('at_symbol', '@')
	mail = mail.replace('dot_symbol', '.')
	try:
		member = Member.objects.filter(
			email = mail).filter(
			member_confirm_id = uid)
		if len(member) > 0:
			member[0].email_confirm = 'confirmed'
			member[0].save()
			return HttpResponse('confirmed')
		else:
			return HttpResponse('no member like this')
	except Exception as ge:
		return HttpResponse("error occured")
