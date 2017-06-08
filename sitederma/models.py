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
    def __str__(self):
        return self.nama_kucing

class Pemilik(models.Model):
    nama = models.CharField(max_length=50)
    alamat = models.CharField(max_length=250, blank=True)
    no_hp = models.CharField(max_length=15, blank=True)
    email = models.CharField(max_length=100, blank=True)
    kucing = models.ForeignKey(Kucing)

    def __str__(self):
        return self.nama

class InfoKlinik(models.Model):
    nama_klinik = models.CharField(max_length=50)
    wilayah = models.CharField(max_length=50)
    alamat = models.CharField(max_length=100)
    no_telp = models.CharField(max_length=15)

    def __str__(self):
        return self.nama_klinik

class InfoPenyakit(models.Model):
    nama_penyakit = models.CharField(max_length=30)
    nama_lain_penyakit = models.CharField(max_length=50)
    info_umum = models.TextField()
    penyebab = models.TextField()
    gejala = models.TextField()
    treatment = models.TextField()
    pencegahan = models.TextField()
    peringatan = models.TextField(blank=True)
    info_penyakit_slug = models.SlugField(max_length=50, null=True)

    def __str__(self):
        return self.nama_penyakit

class ListPenyakit(models.Model):
    kode_penyakit = models.CharField(max_length=5)
    nama_penyakit = models.CharField(max_length=30)
    def __str__(self):
        return self.kode_penyakit

class ListGejala(models.Model):
    kode_gejala = models.CharField(max_length=5)
    nama_gejala = models.CharField(max_length=100)
    def __str__(self):
        return self.kode_gejala

List_Choice = (
        ('1', 'Ya'),
        ('0.5', 'Mungkin'),
        ('0', 'Tidak'),
)

class ListPertanyaan(models.Model):
    indication_1 = models.CharField(
    _('Apakah kucing anda sering menggaruk?'),
    max_length=100,
    null=True,
    choices=List_Choice
    )

    indication_2 = models.CharField(
    _('Apakah kucing anda menggaruk berlebihan?'),
    max_length=100,
    null=True,
    choices=List_Choice
    )

    indication_3 = models.CharField(
    _('Apakah kucing anda menggaruk daerah telinga, leher, dan kepala?'),
    max_length=100,
    null=True,
    choices=List_Choice
    )

    indication_4 = models.CharField(
    _('Apakah kucing anda sering menggeleng-gelengkan kepala?'),
    max_length=100,
    null=True,
    choices=List_Choice
    )

    indication_5 = models.CharField(
    _('Apakah pada telinga kucing anda terdapat kotoran berwarna coklat kehitaman?'),
    max_length=100,
    null=True,
    choices=List_Choice
    )

    indication_6 = models.CharField(
    _('Apakah pada telinga kucing anda terdapat kotoran telinga kering (berpasir) dan tidak berminyak?'),
    max_length=100,
    null=True,
    choices=List_Choice
    )

    indication_7 = models.CharField(
    _('Apakah bulu kucing anda terlihat kusam?'),
    max_length=100,
    null=True,
    choices=List_Choice
    )

    indication_8 = models.CharField(
    _('Apakah bulu kucing anda mengalami kerontokan?'),
    max_length=100,
    null=True,
    choices=List_Choice
    )

    indication_9 = models.CharField(
    _('Apakah bulu pada telinga kucing anda mengalami kerontokan?'),
    max_length=100,
    null=True,
    choices=List_Choice
    )

    indication_10 = models.CharField(
    _('Apakah bulu pada daerah telinga, leher, bahu, pangkal paha, dan daerah dubur kucing anda mengalami kerontokan?'),
    max_length=100,
    null=True,
    choices=List_Choice
    )

    indication_11 = models.CharField(
    _('Apakah bulu kucing anda mengalami kerontokan yang berbentuk melingkar?'),
    max_length=100,
    null=True,
    choices=List_Choice
    )

    indication_12 = models.CharField(
    _('Apakah kulit kucing anda berkerak?'),
    max_length=100,
    null=True,
    choices=List_Choice
    )

    indication_13 = models.CharField(
    _('Apakah kucing anda kulit berkerak kering?'),
    max_length=100,
    null=True,
    choices=List_Choice
    )

    indication_14 = models.CharField(
    _('Apakah kulit pada telinga, siku, kaki, dan perut kucing anda berkerak?'),
    max_length=100,
    null=True,
    choices=List_Choice
    )

    indication_15 = models.CharField(
    _('Apakah kulit kucing anda berdarah?'),
    max_length=100,
    null=True,
    choices=List_Choice
    )

    indication_16 = models.CharField(
    _('Apakah kulit kucing anda bernanah?'),
    max_length=100,
    null=True,
    choices=List_Choice
    )

    indication_17 = models.CharField(
    _('Apakah kulit kucing anda kemerahan?'),
    max_length=100,
    null=True,
    choices=List_Choice
    )

    indication_18 = models.CharField(
    _('Apakah kulit kucing anda terlihat kering?'),
    max_length=100,
    null=True,
    choices=List_Choice
    )

    indication_19 = models.CharField(
    _('Apakah pada kulit kucing anda terdapat luka?'),
    max_length=100,
    null=True,
    choices=List_Choice
    )

    indication_20 = models.CharField(
    _('Apakah pada kulit kucing anda terdapat luka dan lecet di belakang kepala, telinga atau leher?'),
    max_length=100,
    null=True,
    choices=List_Choice
    )

    indication_21 = models.CharField(
    _('Apakah warna kulit kucing anda menjadi kehitaman?'),
    max_length=100,
    null=True,
    choices=List_Choice
    )

    indication_22 = models.CharField(
    _('Apakah pada kucing anda terlihat kutu berwarna merah kecoklatan berjalan cepat di tubuh?'),
    max_length=100,
    null=True,
    choices=List_Choice
    )

    indication_23 = models.CharField(
    _('Apakah pada kucing anda terlihat kotoran hitam seperti pasir di punggung?'),
    max_length=100,
    null=True,
    choices=List_Choice
    )

    indication_24 = models.CharField(
    _('Apakah pada kucing anda terlihat seperti ada butiran di bulu?'),
    max_length=100,
    null=True,
    choices=List_Choice
    )

    indication_25 = models.CharField(
    _('Apakah kucing anda sering menjilat?'),
    max_length=100,
    null=True,
    choices=List_Choice
    )

    indication_26 = models.CharField(
    _('Apakah kucing anda kadang-kadang menjilat kaki dan area tubuh lainnya?'),
    max_length=100,
    null=True,
    choices=List_Choice
    )

    def __str__(self):
        return self.kode_pertanyaan

class Konsultasi(models.Model):
    kodecf = models.CharField(max_length=3)
    penyakit = models.ForeignKey(ListPenyakit)
    gejala = models.ForeignKey(ListGejala)
    bobotcf = models.FloatField()
    def __str__(self):
        return self.kodecf

class Jawaban(models.Model):
    kodejawab = models.CharField(max_length=3)
    jawab = models.CharField(max_length=10)
    bobotjawab = models.FloatField()
    def __str__(self):
        return self.kodejawab
