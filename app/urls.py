from django.urls import path
from .import views

urlpatterns=[
	path('',views.start),
	path('login',views.login),
	path('register',views.register),
	path('regform',views.regform),
	path('perform',views.perform),
	path('perform1',views.perform1),
	path('start1',views.start1),
	path('add',views.addimg),
	path('comment1',views.comment1),
	path('continue1',views.continue1),
	path('confirm',views.confirm),
	]