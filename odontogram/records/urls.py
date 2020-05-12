from django.conf import settings
from django.conf.urls import url
from django.contrib.staticfiles.urls import static

from . import views

app_name = 'records'

urlpatterns = [
    url(r'^$', views.new_odontogram, name='odontogram'),
    url(r'^tooth/$', views.tooth_view, name='tooth'),
]
