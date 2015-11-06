from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import MemberForm


def index(request):
	if request.method == 'POST':

		form = MemberForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			form.save()			
			return render(request, 'regApp/index.html', {'success': 'success'})
		else:
			return render(request, 'regApp/index.html', {'form': form})

	# if a GET (or any other method) we'll create a blank form
	else:
		form = MemberForm()

	return render(request, 'regApp/index.html', {'form': form})