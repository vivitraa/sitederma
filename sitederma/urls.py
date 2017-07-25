from django.conf.urls import url
from . import views
from .forms import LoginForm
from django.contrib.auth.views import login

urlpatterns = [
    #/home_utama/
    url(r'^$', views.home_utama, name='home_utama'),
    url(r'^kontak/$', views.kontak_view, name='kontak'),
    url(r'^bantuan/$', views.help_view, name='help'),
    url(r'^masuk/$', login, name='login', kwargs={"authentication_form" : LoginForm}),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^info_penyakit/$', views.infopenyakit_view, name='infopenyakit'),
    url(r'^daftar/$', views.signup_view, name='signup'),
    url(r'^daftar/sukses/$', views.signupsucces_view, name='signupsucces'),
    url(r'^akun/konfirmasi/(?P<activation_key>\w+)/$', views.account_confirmation_view, name='account_confirmation'),
    url(r'^akun/konfirm/$', views.account_confirmed_view, name='account_confirmed'),
    url(r'^akun/kadaluarsa/$', views.account_expired_view, name='account_expired'),
    url(r'^konsultasi/$', views.konsultasi_view, name='konsultasi'),
    url(r'^riwayat/$', views.riwayat_view, name='riwayat'),
    url(r'^hasil/$', views.hasil_view, name='hasil'),

]
