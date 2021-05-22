from django.shortcuts import render, redirect
from django.contrib import meesages
from .models import User
#home page
def index(request):
    return render(request, 'index.html')
# Create your views here.
#register users
def register(request):
	if request.method =="GET":
		return redirect('/')
	errors = User.objects.validate(request.POST):
	if errors:
		for i in errors.values():
			meesages.error(request, i)
		return redirect('/')
	else:
		new_user = User.object.register(request.POST)
		request.session['user_id'] = new_user.id
		message.success(request, "Successfully registered")
		return redirect('success')
#login
def login(request):
	if request.method =="GET"
		return redirect('/')
	if not User.objects.authenticate(request.POST['email'], request.POST['password']):
		meesages.error(request, 'Invaild email and password combination')
		return redirect('/')
	user = User.objects.get(email=request.POST['email'])
	request.session['user_id'] = user.id
	meesages.success(request, "success")
	return redirect('/success')
#logout
def logout(request):
	request.session.clear()
	return redirect('/')
#brings you to the page saying you successfully signed up
def success(request):
	if 'user_id' not in request.session:
		return redirect('/')
	user= User.objects.get(id=request.session['user_id'])
	context = {
		'user': user
	}
	return render(request, 'success.html', context)

