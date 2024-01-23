from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from .models import RegistrationForm


# Create your views here.
def index(request):
    return render(request,"index.html")

def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("Detail")
        else:
            messages.info(request,'invalid snaps')
            return redirect('/')
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['confirmPassword']
        if password==cpassword:
           if User.objects.filter(username=username).exists():
               messages.info(request,"Username Taken")
               return redirect('register')
           else:
             user = User.objects.create_user(username=username,password=password)

             user.save();
             return redirect('login')
        else:
           messages.info(request,'password not maching')
           return  redirect('register')
        return   redirect('/')
    return render(request, "register.html")
def commerce(request):
    return render(request,"commerce.html")
def computer(request):
    return render(request,"computer.html")
def eco(request):
    return render(request,"eco.html")
def eng(request):
    return render(request,"eng.html")
def phy(request):
    return render(request,"phy.html")
def chemistry(request):
    return render(request,"chemistry.html")


def Detail(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():

            return redirect('order confirmed')
        else:
            form = RegistrationForm()

    return render(request, 'form.html')



