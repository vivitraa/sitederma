from django.contrib import admin
from .models import Kucing, InfoKlinik, InfoPenyakit, ListGejala, Konsultasi, Jawaban, ListTanya

class KucingAdmin(admin.ModelAdmin):
    list_display = ['nama_kucing', 'umur_kucing', 'gender_kucing',]
    search_fields = ['nama_kucing']
    list_per_page = 25
admin.site.register(Kucing, KucingAdmin)

class InfoKlinikAdmin(admin.ModelAdmin):
    list_display = ['nama_klinik', 'wilayah', 'alamat', 'no_telp',]
    search_fields = ['nama_klinik', 'wilayah',]
    list_per_page = 25
admin.site.register(InfoKlinik, InfoKlinikAdmin)

class InfoPenyakitAdmin(admin.ModelAdmin):
    list_display = ['kode_penyakit', 'nama_penyakit', 'info_umum', 'penyebab', 'gejala', 'pengobatan', 'pencegahan', 'peringatan',]
    search_fields = ['nama_penyakit']
    list_per_page = 25
admin.site.register(InfoPenyakit, InfoPenyakitAdmin)

class ListTanyaAdmin(admin.ModelAdmin):
    list_display = ['kode_tanya', 'daftar_tanya', 'kode_gejala']
    search_fields = ['daftar_tanya']
    list_per_page = 25
admin.site.register(ListTanya, ListTanyaAdmin)

class ListGejalaAdmin(admin.ModelAdmin):
    list_display = ['kode_gejala', 'nama_gejala',]
    search_fields = ['nama_gejala']
    list_per_page = 25
admin.site.register(ListGejala, ListGejalaAdmin)

class KonsultasiAdmin(admin.ModelAdmin):
    list_display = ['kodecf','kode_penyakit','kode_gejala','cfp',]
    search_fields = ['cfp']
    list_per_page = 25
admin.site.register(Konsultasi, KonsultasiAdmin)

class JawabanAdmin(admin.ModelAdmin):
    list_display = ['kodejawab', 'jawab', 'bobotjawab',]
    search_fields = ['kodejawab']
    list_per_page = 25
admin.site.register(Jawaban, JawabanAdmin)
