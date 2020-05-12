from django.conf import settings
from django.conf.urls import url
from django.contrib.staticfiles.urls import static

from . import views

app_name = 'records'

urlpatterns = [
    url(r'^$',
        views.ask_odontogram, name='ask_odontogram'
    ),
    #url(r'^new_odonto_(?P<pk_mouth>\d+)/$',
    url(r'^new_odonto/$',
        views.new_odontogram, name='new_odontogram'
    ),
    url(r'^odonto_(?P<pk_mouth>\d+)/tooth_(?P<nb_tooth>\w+)/$',
        views.tooth_view, name='tooth'
    ),
    url(r'^odonto_(?P<pk_mouth>\d+)/$',
        views.update_odonto, name='update_odontogram'
    ),
]
