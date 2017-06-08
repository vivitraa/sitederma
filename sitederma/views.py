from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from .models import InfoPenyakit
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from .forms import SignupForm
import hashlib, datetime, random
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import UserActivationKey, ListPertanyaan
from django.utils import timezone

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

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def konsultasi_view(request):
    indications = ListPertanyaan.objects.all()
    context = {}
    context ['indications'] = indications
    return render(request, "sitederma/mulai_konsul.html", context)

def riwayat_view(request):
    return render(request, "sitederma/riwayat.html")
