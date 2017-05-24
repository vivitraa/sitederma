from django.conf.urls import url
from . import views
from .forms import LoginForm
from django.contrib.auth.views import login

urlpatterns = [
    #/home_utama/
    url(r'^$', views.home_utama, name='home_utama'),
    url(r'^kontak/$', views.kontak_view, name='kontak'),
    url(r'^help/$', views.help_view, name='help'),
    url(r'^login/$', login, name='login', kwargs={"authentication_form" : LoginForm}),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^info-penyakit/$', views.infopenyakit_view, name='infopenyakit'),
    url(r'^daftar/$', views.signup_view, name='signup'),
    url(r'^daftar/sukses/$', views.signupsucces_view, name='signupsucces'),
]
