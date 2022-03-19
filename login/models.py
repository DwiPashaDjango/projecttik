from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
# Create your models here.


class Pengunjung(models.Model):
    username = models.CharField(max_length=60)
    kls = models.CharField(max_length=70)
    tanggal = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.username


class Kelas(models.Model):
    kls = models.CharField(max_length=50)

    def __str__(self):
        return self.kls


class User(AbstractUser):
    is_admin = models.BooleanField('is_admin', default=False)
    is_petugas = models.BooleanField('is_petugas', default=False)
    is_siswa = models.BooleanField('is_siswa', default=False)
    kelas_id = models.ForeignKey(Kelas, on_delete=models.CASCADE, null=True)


class Kelompok(models.Model):
    nama = models.CharField(max_length=20)
    keterangan = models.TextField()

    def __str__(Self):
        return Self.nama


class Buku(models.Model):
    judul = models.CharField(max_length=50)
    penulis = models.CharField(max_length=40)
    penerbit = models.CharField(max_length=40)
    jumlah = models.IntegerField(null=True)
    kelompok_id = models.ForeignKey(
        Kelompok,
        on_delete=models.CASCADE,
        null=True
    )
    cover = models.ImageField(upload_to='cover/', null=True)
    tanggal = models.DateField(auto_now_add=True, null=True)
    keterangan = models.TextField(null=True)

    def __str__(self):
        return self.judul


class Pinjam(models.Model):
    judul = models.CharField(max_length=50)
    nama = models.CharField(max_length=50)
    kelas = models.CharField(max_length=50)
    tanggal = models.DateField(max_length=40)
    t_pengembalian = models.DateField(max_length=50, null=True)

    def __str__(self):
        return self.nama


class Pengembalian(models.Model):
    nama = models.CharField(max_length=50)
    judul = models.CharField(max_length=50)
    kelas = models.CharField(max_length=50)
    tanggal = models.DateField(max_length=40, auto_now_add=True)

    def __str__(self):
        return self.nama


class Request(models.Model):
    nama = models.CharField(max_length=20, null=True)
    judul = models.CharField(max_length=30)
    kelas = models.CharField(max_length=30)
    tanggal = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama
