from django.shortcuts import render, get_object_or_404, redirect
from .models import InfoPenyakit
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from .forms import SignupForm

def home_utama(request):
    return render(request, "sitederma/home_utama.html")

def kontak_view(request):
    return render(request, "sitederma/kontak.html")

def help_view(request):
    return render(request, "sitederma/help.html")

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

            user_profile = UserProfile(user=user)
            user_profile.save()

            host=request.META['HTTP_HOST']
            email_subject = 'Konfirmasi Akun'
            email_body = "Halo {}, terima kasih. http://{}/akun/konfirmasi/{}".format(username, host, activation_key)

            from_email = settings.EMAIL_HOST_USER
            to_email = [user.email, settings.EMAIL_HOST_USER]

            send_mail(email_subject, email_body, from_email, to_email, fail_silently=False)

            return HttpResponseRedirect('/daftar/sukses')

        else:
            form = SignupForm()

        return render(request, 'sitederma/signup.html', {'form': form})

def signupsucces_view(request):
    return render(request, "sitederma/signupsucces.html")

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
