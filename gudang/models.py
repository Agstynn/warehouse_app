from django.db import models

class Barang(models.Model):
    kode = models.CharField(max_length=20, unique=True)
    nama = models.CharField(max_length=100)
    stok = models.PositiveIntegerField(default=0)
    satuan = models.CharField(max_length=20)
    tanggal_masuk = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.kode} - {self.nama}"


class Transaksi(models.Model):
    JENIS_CHOICES = [
        ('masuk', 'Masuk'),
        ('keluar', 'Keluar'),
    ]
    barang = models.ForeignKey(Barang, on_delete=models.CASCADE)
    jumlah = models.PositiveIntegerField()
    jenis = models.CharField(max_length=10, choices=JENIS_CHOICES)
    tanggal = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.jenis} - {self.barang.kode} - {self.jumlah}"

    def save(self, *args, **kwargs):
        """
        Update stok Barang otomatis saat transaksi baru dibuat.
        Jika transaksi keluar, pastikan stok cukup.
        """
        if not self.pk:  # hanya untuk transaksi baru
            if self.jenis == 'masuk':
                self.barang.stok += self.jumlah
            elif self.jenis == 'keluar':
                if self.barang.stok < self.jumlah:
                    raise ValueError("Stok tidak cukup!")
                self.barang.stok -= self.jumlah
            self.barang.save()  # simpan perubahan stok
        super().save(*args, **kwargs)
