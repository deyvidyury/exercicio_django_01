from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name="home"),
	url(r'^question/(?P<question_id>\d+)/$', views.question, name="question"),
	url(r'^question/(?P<question_id>\d+)/results/$', views.results, name="results"),
	url(r'^question/(?P<question_id>\d+)/manage/$', views.manage, name="manage"),
	url(r'^question/(?P<question_id>\d+)/change_status/$', views.change_status, name="change_status"),
	url(r'^question/(?P<question_id>\d+)/vote/(?P<choice_id>\d+)/$', views.vote, name="vote"),
	url(r'^question/(?P<question_id>\d+)/add/(?P<choice_id>\d+)/$', views.add, name="add"),
	url(r'^question/(?P<question_id>\d+)/remove/(?P<choice_id>\d+)/$', views.remove, name="remove"),
]