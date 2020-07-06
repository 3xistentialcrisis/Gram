from django.conf.urls import url, include
from django.contrib import admin
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'', include('instaclone.urls')),
    url(r'^tinymce/', include('tinymce.urls'))
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

