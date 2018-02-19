from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.http import HttpResponse

from .models import ContactInfo
from django.utils import timezone

# Create your views here.
def index(request):
	return render(request, 'index.html')

def contact(request):
	if request.method == 'POST':
		# print(request.POST)
		data = request.POST
		info = ContactInfo(first_name=data['first_name'], last_name=data['last_name'],
			email=data['email'], phone=data['phone'], message=data['message'], 
			date_time=timezone.now())
		info.save()

		return redirect('/receive/')

	else:
		return render(request, 'contact.html')

def receive_message(request):
	return render(request, 'receive_message.html')
