from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
import datetime

class UserActivationKey(models.Model):
    user = models.OneToOneField(User)
    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField(default=datetime.date.today())
    def __str__(self):
        return self.user.username

class Kucing(models.Model):
    GENDER_KUCING_CHOICES = (
    ('betina', 'Betina'),
    ('jantan', 'Jantan'),
    )

    nama_kucing = models.CharField(max_length=30)
    umur_kucing = models.CharField(max_length=10)
    gender_kucing = models.CharField(max_length=10, choices=GENDER_KUCING_CHOICES)
    pemilik = models.ForeignKey(User, null=True)
    def __str__(self):
        return self.nama_kucing

class InfoKlinik(models.Model):
    nama_klinik = models.CharField(max_length=50)
    wilayah = models.CharField(max_length=50)
    alamat = models.TextField()
    no_telp = models.CharField(max_length=15)

    def __str__(self):
        return self.nama_klinik

class InfoPenyakit(models.Model):
    kode_penyakit = models.CharField(max_length=5, null=True)
    nama_penyakit = models.CharField(max_length=30)
    info_umum = models.TextField()
    penyebab = models.TextField()
    gejala = models.TextField()
    pengobatan = models.TextField()
    pencegahan = models.TextField()
    peringatan = models.TextField(blank=True)

    def __str__(self):
        return self.kode_penyakit

class ListGejala(models.Model):
    kode_gejala = models.CharField(max_length=5)
    nama_gejala = models.CharField(max_length=100)
    def __str__(self):
        return self.kode_gejala

class ListTanya(models.Model):
    kode_tanya = models.CharField(max_length=5)
    kode_gejala = models.ForeignKey(ListGejala, related_name = 'tanya_gejala', null=True)
    no_tanya = models.CharField(max_length=2, null=True)
    daftar_tanya = models.CharField(max_length=150)
    def __str__(self):
        return self.daftar_tanya

class Konsultasi(models.Model):
    kodecf = models.CharField(max_length=3)
    kode_penyakit = models.ForeignKey(InfoPenyakit, null=True)
    kode_gejala = models.ForeignKey(ListGejala)
    cfp = models.FloatField()
    def __str__(self):
        return self.kodecf

class Jawaban(models.Model):
    kodejawab = models.CharField(max_length=3)
    jawab = models.CharField(max_length=10)
    bobotjawab = models.FloatField()
    def __str__(self):
        return self.jawab
