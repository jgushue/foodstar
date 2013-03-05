from django.conf.urls import patterns, url
from lists import views

urlpatterns = patterns('',
	url(r'^index/$', views.index, name='index'),
	url(r'^fresh/$', views.fresh, name='fresh'),
)