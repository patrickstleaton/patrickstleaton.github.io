from django.conf.urls import url
from my_app import views

app_name = 'my_app'

urlpatterns = [
url(r'^$',views.HospitalListView.as_view(), name='list'),
url(r'^(?P<pk>[-\d]+)/$', views.HospitalDetailView.as_view(), name='detail'),
url(r'^update/(?P<pk>\d+)/$', views.HospitalUpdateView.as_view(), name='update'),
url(r'^create/$', views.HospitalCreateView.as_view(), name = 'create'),
url(r'^delete/(?P<pk>\d+)/$', views.HospitalDeleteView.as_view(), name='delete')
]
