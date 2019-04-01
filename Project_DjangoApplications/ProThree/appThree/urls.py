from django.conf.urls import url
from appThree import views

urlpatterns = [
url(r'^$', views.users,name='users'),
]
