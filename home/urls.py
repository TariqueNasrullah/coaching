from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^courses/science$', views.course_view_science, name='course_view_science'),
	url(r'^courses/commerce$', views.course_view_commerce, name='course_view_commerce'),
	url(r'^courses/arts$', views.course_view_arts, name='course_view_arts'),
	url(r'^events/$', views.events, name='events'),
	url(r'^events/(?P<pk>\d+)/$', views.events_param, name='events_param'),
	url(r'^teachers$', views.teachers, name='teachers'),
	url(r'^contact$', views.contact, name='contact'),
	url(r'^test/(?P<pk>\d+)/$', views.test, name='test'),
]