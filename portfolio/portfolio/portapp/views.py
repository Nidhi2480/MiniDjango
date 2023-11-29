from django.shortcuts import render,redirect
from . models import profile
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.
def index(request):
    # return HttpResponse('hello')
    obj=profile.objects.all()
    return render(request,'index.html',{'profile':obj})
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return render(request,'login')
    else:
        return render(request,'login.html')



def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
    
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exists')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save()
                messages.success(request,'registration success')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request,'reg.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')