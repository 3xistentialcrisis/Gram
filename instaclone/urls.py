from django.conf.urls import url, include
from . import views
from instaclone.views import PostLikeToggle, PostLikeAPIToggle
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views


app_name = 'instaclone'

urlpatterns = [
    url('^$', views.index, name='index'),
    url(r'signup/', views.signup, name='signup'),
    # url(r'login/', views.login, name='login'),
    # url(r'accounts/login/', auth_views.LoginView.as_view()),
    url(r'account/', include('django.contrib.auth.urls')),
    url(r'profile/(?P<username>pattern)', views.profile, name='profile'),
    url(r'user_profile/<username>/', views.user_profile, name='user_profile'),
    url(r'post/<id>', views.post_comment, name='comment'),
    url(r'post/<id>/like', PostLikeToggle.as_view(), name='liked'),
    url(r'api/post/<id>/like', PostLikeAPIToggle.as_view(), name='liked-api'),
    url(r'like', views.like_post, name='like_post'),
    url(r'search/', views.search_profile, name='search'),
    url(r'unfollow/<to_unfollow>', views.unfollow, name='unfollow'),
    url(r'follow/<to_follow>', views.follow, name='follow'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
