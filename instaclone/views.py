from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.contrib.auth import login, authenticate

# Create your views here.
#Index Page
def index(request):
    return render(request, 'instaclone/index.html')

#Signup Page    
def signup(request):
   if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required(login_url='login')
def index(request):
    return render(request, 'instaclone/index.html')

@login_required
def profile(request):
    user = request.user
    return render(request, 'instaclone/profile.html',{'user':user})