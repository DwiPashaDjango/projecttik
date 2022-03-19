from django.contrib import admin
from .models import Kelas, Pengembalian, Pengunjung, Pinjam, Request, User, Kelompok, Buku

# Register your models here.
admin.site.register(User)
admin.site.register(Buku)
admin.site.register(Kelompok)
admin.site.register(Pinjam)
admin.site.register(Pengembalian)
admin.site.register(Request)
admin.site.register(Kelas)
admin.site.register(Pengunjung)
