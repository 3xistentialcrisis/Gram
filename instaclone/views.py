from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm,UpdateUserForm, UpdateUserProfileForm
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

@login_required(login_url='login')
def profile(request, username):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.FILES, request.POST, instance=request.user.profile)
        
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            redirect('profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
    params = {
        'user_form': user_form,
        'prof_form': prof_form,
    }
    return render(request, 'instaclone/profile.html', params)