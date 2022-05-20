from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import User,Profile
from django.contrib.auth.forms import PasswordChangeForm
from .forms import Profileform, UserCreationForm
from django.contrib import messages
# Create your views here.

def home_view(request):
    context= {}
    return render(request,'home.html',context)

def login_view(request):
    page = 'login'
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request,'user does not exist')
        user = authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.error(request,'incorrect email or password')
    
    context={'page':page}
    return render(request,'accounts/login_register.html',context)

def register_view(request):
    form = UserCreationForm
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            user = form.save(commit=False)
            user.email = user.email.lower()
            user = form.save()
            login(request,user)
            return redirect('/create')
        else:
            messages.error(request,'Some error accuired')

    context={'form':form}
    return render(request,'accounts/login_register.html',context)

def logout_view(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login')
def profile_view(request):
    # profile = request.user.Profile()
    context={}
    return render(request,'accounts/profiles.html',context)

@login_required(login_url='/login')
def create_profile(request):
    form = Profileform
    if request.method == 'POST':
        form = Profileform(request.POST, files=request.FILES)
        if form.is_valid:
            profile = form.save(commit=False)
            profile.user = request.user
            profile = form.save()
            return redirect('/')
        else:
            messages.error('some error accuired')
    
    context={'form':form}
    return render(request,'accounts/create_profile.html',context)

@login_required(login_url='/login')
def update_profile(request):
    try:
        obj = Profile.objects.get(user = request.user)
    except:
        return redirect('/create')
    form = Profileform(instance=obj)
    if request.method == 'POST':
        form = Profileform(request.POST, files=request.FILES,instance=obj)
        if form.is_valid:
            form.save()
            return redirect('/')
    context ={'form':form}
    return render(request,'accounts/create_profile.html',context)

def changepassword(request):
    form = PasswordChangeForm(user=request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user,data =request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash
        else:
            messages.error(request,'Some error accuired')
    
    context = {'form':form}
    return render(request,'accounts/change_password.html',context)
