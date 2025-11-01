from django.contrib import admin
from .models import Barang, Transaksi


@admin.register(Barang)
class BarangAdmin(admin.ModelAdmin):
    list_display = ('kode', 'nama', 'stok', 'satuan', 'tanggal_masuk')
    search_fields = ('kode', 'nama')


@admin.register(Transaksi)
class TransaksiAdmin(admin.ModelAdmin):
    list_display = ('barang', 'jenis', 'jumlah', 'tanggal')
    list_filter = ('jenis',)
    search_fields = ('barang__kode', 'barang__nama')
