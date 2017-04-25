from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'', views.ui, name='ui'),
    url(r'', views.channels_page),
]