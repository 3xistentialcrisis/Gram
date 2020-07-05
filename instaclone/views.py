from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#Index Page
def index(request):
    return render(request, 'instaclone/index.html')

#Signup Page    
def signup(request):
    return render(request, 'registration/signup.html')