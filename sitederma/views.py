from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import SignupForm, KucingForm, RiwayatForm
import hashlib, datetime, random
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import UserActivationKey, ListTanya, InfoPenyakit, Jawaban, ListGejala, Konsultasi, InfoKlinik, Kucing
from django.utils import timezone
from collections import defaultdict
import operator

def home_utama(request):
    return render(request, "sitederma/home_utama.html")

def kontak_view(request):
    return render(request, "sitederma/kontak.html")

def help_view(request):
    return render(request, "sitederma/bantuan.html")

def infopenyakit_view(request):
    info_penyakit = InfoPenyakit.objects.all()
    gejala = ListGejala.objects.all()
    kode = Konsultasi.objects.all()
    context = {}
    context ['info_penyakit'] = info_penyakit
    context ['gejala'] = gejala
    context ['kode'] = kode
    return render(request, "sitederma/infopenyakit.html", context)

def infoklinik_view(request):
    info_klinik = InfoKlinik.objects.all()
    context = {}
    context ['info_klinik'] = info_klinik
    return render(request, "sitederma/infoklinik.html", context)

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

def profil_view(request):
    return render(request, "sitederma/profil.html")


def inputkucing_view(request):
    infokucing = Kucing.objects.all()
    context = {}
    context ['infokucing'] = infokucing

    if request.method == 'POST':
        form = KucingForm(request.POST)
        if form.is_valid():
            kucing = form.save(commit=False)
            kucing.username = request.user
            kucing.save()

            return HttpResponseRedirect('/input_kucing/')
    else:
        form = KucingForm()

    return render(request, 'sitederma/inputkucing.html', {'form': form})

def konsultasi_view(request):
    diagnosa = None
    list_tanya = ListTanya.objects.all()
    list_pilihan = Jawaban.objects.all()
    gejala = ListGejala.objects.all()
    context = {}
    context ['list_tanya'] = list_tanya
    context ['list_pilihan'] = list_pilihan

    if request.method=='POST':
        formriwayat = RiwayatForm(request.POST)
        d = defaultdict(float)
        d = {}
        cfgp1_={}
        percentdisease = {}
        counter = 1

        for cfuser in gejala:
            d['cfug_%02d' % counter] = float(request.POST.get(cfuser.kode_gejala))
            counter += 1
        for key, value in sorted(d.items()):
            print (key, value)
        penyakit = InfoPenyakit.objects.all()
        gej_pen = Konsultasi.objects.all()

        for pen in penyakit:
            cfglama = None
            cfgbaru = None
            cfgkombinasi = None
            for gejala_penyakit in gej_pen:
                if gejala_penyakit.kode_penyakit.kode_penyakit == pen.kode_penyakit:
                    print('ya')
                    urut = gejala_penyakit.kode_gejala.kode_gejala[1:]
                    print(urut)
                    cfgp1_['cfg{0}'.format(urut)] = d['cfug_{}'.format(urut)] * gejala_penyakit.cfp
                    if not cfglama:
                        cfglama = cfgp1_['cfg{0}'.format(urut)]
                    else :
                        cfgbaru = cfgp1_['cfg{0}'.format(urut)]
                        cfgkombinasi = cfglama+(cfgbaru*(1-cfglama))
                        cfglama = cfgkombinasi
                    percentdisease['pdisease{0}'.format(pen.kode_penyakit)] = cfgkombinasi
                    print(percentdisease)
        context['percentdisease_1'] = percentdisease['pdisease{0}'.format('P1')]
        context['percentdisease_2'] = percentdisease['pdisease{0}'.format('P2')]
        context['percentdisease_3'] = percentdisease['pdisease{0}'.format('P3')]
        context['percentdisease_4'] = percentdisease['pdisease{0}'.format('P4')]
        context['percentdisease_5'] = percentdisease['pdisease{0}'.format('P5')]
        context['percentdisease_6'] = percentdisease['pdisease{0}'.format('P6')]
        targetdisease = max(percentdisease, key=percentdisease.get)
        context['targetdisease'] = targetdisease
        if targetdisease == "diseaseP1":
            diagnosa ='Ear Mites'
        elif targetdisease == "diseaseP2":
            diagnosa = 'Flea'
        elif targetdisease == "diseaseP3":
            diagnosa = 'Lice'
        elif targetdisease == "diseaseP4":
            diagnosa = 'Pyoderma'
        elif targetdisease == "diseaseP5":
            diagnosa = 'Ringworm'
        elif targetdisease == "diseaseP6":
            diagnosa = 'Scabies'
        request.session['percentdisease'] = {
                                        'percentdisease_1': context['percentdisease_1'],
                                        'percentdisease_2': context['percentdisease_2'],
                                        'percentdisease_3': context['percentdisease_3'],
                                        'percentdisease_4': context['percentdisease_4'],
                                        'percentdisease_5': context['percentdisease_5'],
                                        'percentdisease_6': context['percentdisease_6'],
                                        'targetdisease': context['targetdisease'],
                                        }
        if formriwayat.is_valid():
            kucing = formriwayat.save(commit=False)
            kucing.username = request.user
            kucing.tanggal_diagnosa = timezone.now()
            kucing.hasil_diagnosa = diagnosa
            kucing.save()
            return HttpResponseRedirect(reverse('sitederma:hasil'))
    else:
        formriwayat = RiwayatForm()
    context['formriwayat']=formriwayat
    return render(request, "sitederma/mulai_konsul.html",  context)

def hasil_view(request):
    context = request.session.get('percentdisease')

    return render(request, "sitederma/halaman_hasil.html", context)

def riwayat_view(request):
    return render(request, "sitederma/riwayat.html")

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
