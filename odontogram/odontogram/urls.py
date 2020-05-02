from django.contrib import admin
from django.conf import settings
from django.conf.urls import include, url
from django.contrib.staticfiles.urls import static

from . import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^records/', include('records.urls', namespace='record')),
]
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
