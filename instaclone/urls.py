from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'instaclone'

urlpatterns = [
    # url(r'^instaclone/', views.index, name='index'),
    url(r'signup/', views.signup, name='signup'),
    url(r'account/', include('django.contrib.auth.urls')),
    url('', views.index, name='index'),
    url(r'profile/<username>/', views.profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)