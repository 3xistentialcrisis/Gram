from django.conf.urls import url
from . import views

app_name = 'instaclone'

urlpatterns = [
    url(r'^instaclone/', views.index, name='index'),
    url(r'signup/', views.signup, name='signup')
]