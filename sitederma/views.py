from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import SignupForm
import hashlib, datetime, random
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import UserActivationKey, ListTanya, InfoPenyakit, Jawaban, ListGejala, Konsultasi
from django.utils import timezone
from collections import defaultdict

def home_utama(request):
    return render(request, "sitederma/home_utama.html")

def kontak_view(request):
    return render(request, "sitederma/kontak.html")

def help_view(request):
    return render(request, "sitederma/bantuan.html")

def infopenyakit_view(request):
    info_penyakit = InfoPenyakit.objects.all()
    context = {}
    context ['info_penyakit'] = info_penyakit
    return render(request, "sitederma/infopenyakit.html", context)

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            username = form.cleaned_data['username']
            email = form.cleaned_data['email']

            activation_key = hashlib.sha224((email).encode('utf-16be')).hexdigest()
            key_expires = datetime.datetime.today() + datetime.timedelta(2)

            user=User.objects.get(username=username)
            user_activation_key = UserActivationKey(user=user, activation_key=activation_key, key_expires=key_expires)
            user_activation_key.save()

            host=request.META['HTTP_HOST']
            email_subject = 'Konfirmasi Akun'
            email_body = "Halo {}, Terima kasih telah melakukan pendaftaran di Sitederma. Selamat datang di aplikasi sitederma. Untuk melanjutkan silahkan melakukan aktivasi akun anda dengan klik pada link di bawah kurang daei 48 jam.\
             http://{}/akun/konfirmasi/{}".format(username, host, activation_key)

            from_email = settings.EMAIL_HOST_USER
            to_email = [user.email, settings.EMAIL_HOST_USER]

            send_mail(email_subject, email_body, from_email, to_email, fail_silently=False)

            return HttpResponseRedirect('/daftar/sukses')

    else:
        form = SignupForm()

    return render(request, 'sitederma/signup.html', {'form': form})


def signupsucces_view(request):
    return render(request, "sitederma/signupsucces.html")

def account_confirmation_view(request, activation_key):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/home_utama.html')

    user_activation = get_object_or_404(UserActivationKey, activation_key=activation_key)
    if user_activation.key_expires < timezone.now():
        return render_to_response('/account_expired.html')
    user = user_activation.user
    user.is_active = True
    user.save()
    return render_to_response('sitederma/account_confirmed.html')

def account_confirmed_view():
    return render(request, "sitederma/account_confirmed.html")

def account_expired_view():
    return render(request, "sitederma/account_expired.html")

def konsultasi_view(request):
    list_tanya = ListTanya.objects.all()
    list_pilihan = Jawaban.objects.all()
    gejala = ListGejala.objects.all()
    penyakit = InfoPenyakit.objects.all()
    gej_pen = Konsultasi.objects.all()
    context = {}
    context ['list_tanya'] = list_tanya
    context ['list_pilihan'] = list_pilihan

    if request.method=='POST':
        d = defaultdict(float)
        d = {}
        # cfgp penyakit 1
        # cfgp1_= defaultdict(float)
        cfgp1_={}

        counter = 1
        for cfuser in gejala:
            d['cfug_%02d' % counter] = request.POST.get(cfuser.kode_gejala)
            counter += 1
            # print (request.POST)

        for penyakit in penyakit:
            for gejala_penyakit in gej_pen:
                if gejala_penyakit.kode_penyakit == penyakit.kode_penyakit:
                    urut = int(gejala_penyakit.kode_penyakit[-2])
                    cfgp1_['cfg{0}'.format(urut)] = cfug_[urut] * gejala_penyakit.bobotcf

        for key, value in sorted(d.items()):
            print (key, value)
        for key, value in sorted(cfgp1_.items()):
            print (key, value)

        #return HttpResponseRedirect(reverse('sitederma:hasil'))

    return render(request, "sitederma/mulai_konsul.html", context)

def hasil_view(request):
    return render(request, "sitederma/halaman_hasil.html")

def riwayat_view(request):
    return render(request, "sitederma/riwayat.html")

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
