from django.db import models

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

class ListPertanyaan(models.Model):
    kode_pertanyaan = models.CharField(max_length=5)
    pertanyaan = models.TextField()
    gejala = models.ForeignKey(ListGejala)
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