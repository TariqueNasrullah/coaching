from . import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('home.urls')),
    url(r'^photologue/', include('photologue.urls', namespace='photologue')),
    url(r'^tinymce/', include('tinymce.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)