from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import MemberForm
from .models import Member
from .helpers import sendMail, generateUID, getConfirmationLink


def index(request):
	if request.method == 'POST':

		form = MemberForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			newMember = form.save()
			newMember.email_confirm = 'uncomfirmed'
			newMember.member_confirm_id = str(generateUID())	
			try:
				sendMail('ახალი პოლიტიკური ცენტრი', 
					[newMember.email],
					'თუ თქვენ შეავსეთ ახალ პოლიტიკურ ცენტრში გაწევრიანების ფორმა ' + 
					'გთხოვთ დაადასტუროთ შემდეგ მისამართზე დაჭერით ' + 
					str(getConfirmationLink()))
			except Exception as ge:
				newMember.email_confirm = 'fail'
			newMember.save()
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
	mail = mail.replace('atsymbol', '@')
	try:
		member = Member.objects.filter(
			email = mail).filter(
			member_confirm_id = uid)
		if len(member) > 0:
			member.email_confirm = 'confirmed'
			member.save()
	except Exception as ge:
		print(str(ge))
		return HttpResponse("error ")