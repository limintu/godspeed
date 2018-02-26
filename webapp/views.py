from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.http import HttpResponse
from django.utils import timezone
# from django.urls import reverse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, UserManager
from django.contrib.auth.decorators import login_required


from .models import ContactInfo
from .forms import ContactForm

from webapp.utils.username_generator import generate_username


# Create your views here.

### Index Page ###
def index(request):
	return render(request, 'index.html')

### Contact_Me Page ###
def contact(request):
	if request.method == 'POST':
		data = request.POST
		info = ContactInfo(first_name=data['first_name'], last_name=data['last_name'],
			email=data['email'], phone=data['phone'], message=data['message'], 
			date_time=timezone.now())
		info.save()

		return redirect('/receive/')

	else:
		# form = ContactForm()
		return render(request, 'contact.html', {'form': form})

### Page of receiving message ###
def receive_message(request):
	return render(request, 'receive_message.html')

def signup(request):
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		password_confirm = request.POST['password_confirm']
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		Phone = request.POST['phone']
		
		if password != password_confirm:
			print ("!!! pssowrd not match !!!")
			errors = {'password_not_match': 'password not match'}
			return render(request, 'accounts/signup.html', errors)

		user = User.objects.create_user(
			username = generate_username(10),
			email = email,
			password = password,
			first_name = first_name,
			last_name = last_name
			)

		print ("!!! user created !!!")

		return redirect('/')

	else:
		return render(request, 'accounts/signup.html')

@login_required(login_url='/accounts/login/')
def dashboard(request):
		print(str(request.user.first_name) + " is logging in")
		return render(request, 'accounts/dashboard.html')

def auth_login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		
		# GET the previous URL when not logging in
		action_after_login = request.GET.get('next')
		# print (action_after_login)
		
		if user is not None:
			login(request, user)
			print ("!!!!! User Exists and Login !!!!!")
			return redirect(action_after_login)
		else:
			print ("!!!!! Invalid User !!!!!")
			context = {'username': username, 'invalid_password': "Invalid Password"}
			return render(request, 'accounts/login.html', context)
	else:
		action_after_login = request.GET.get('next')
		print (action_after_login)
		return render(request, 'accounts/login.html')

@login_required(login_url='/accounts/login/')
def password_change(request):
	if request.method == 'POST':
		rediect('/')
	else:
		context = {'user': request.user}
		return render(request, 'accounts/password_change.html', context)

def password_change_done(request):
	return render(request, 'accounts/password_change_done.html')

def auth_logout(request):
    logout(request)
    return redirect('index')
    # Redirect to a success page.

