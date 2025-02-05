from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.core.exceptions import ValidationError
import re



# Create your views here.

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.error(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')



   
def register(request):

    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already taken')
                return redirect('register')
            
            elif not re.match(r"^[a-zA-Z0-9_.+-]+@(gmail\.com|yahoo\.com)$", email):
                messages.info(request, "Please use a valid email address with @gmail.com or @yahoo.com ")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                messages.info(request,'user created')
                return redirect('login')
                
        else:
            messages.info(request,'password not matching') 
            return redirect('register')   
        # return redirect('/')
    else:    
        return render(request,'register.html')
    
def logout(request):
    auth.logout(request)
    if 'viewed_destinations' in request.session:
        del request.session['viewed_destinations']
    # return redirect('home')
    return redirect('/')