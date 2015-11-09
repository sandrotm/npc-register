from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^confirm/(?P<mail>\w+)/(?P<uid>\w+)/$', views.confirm, name = 'confirm'),
	]