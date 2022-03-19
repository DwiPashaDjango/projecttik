from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from login.viewset_api import *
from rest_framework import routers
from django.contrib.auth.views import LogoutView

router = routers.DefaultRouter()
router.register('buku', Bukuviewset)

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    # path('daftar/', views.daftar, name='daftar'),
    # path('keluar/', views.__loader__(next_page='masuk'), name='keluar'),

    # api
    path('api/', include(router.urls)),

    # page admin
    path('home_admin/', views.home_admin, name='home_admin'),
    path('tambahPetugas/', views.tambahPetugas, name='tambahPetugas'),
    path('tambah_buku/', views.tambah_buku, name='tambah_buku'),
    path('s_buku/', views.s_buku, name='s_buku'),
    path('buku/ubah/<int:id_buku>', views.ubah, name='ubah'),
    path('buku/hapus/<int:id_buku>', views.hapusbuku, name='hapusbuku'),
    path('d_peminjam/', views.d_peminjam, name='d_peminjam'),
    path('pinjam/hapus/<int:id_peminjam>', views.hapus_p, name='hapus_p'),
    path('pengembalian_user/', views.pengembalian_user, name='pengembalian_user'),
    path('pngbl/hapus/<int:id_pengembalian>',
         views.hapus_pngbl, name='hapus_pngbl'),
    path('profile_admin', views.profile_admin, name='profile_admin'),
    path('d-request/', views.d_request, name='d_request'),
    path('rqst/hapus/<int:id_request>', views.r_hapus, name='r_hapus'),
    path('d_user/', views.d_user, name='d_user'),
    path('user/hps/<int:id_user>', views.u_hapus, name='u_hapus'),
    path('export/xls/', views.export_xls, name='export_xls'),
    path('export_2/peminjam/', views.e_datapeminjam, name='e_datapeminjam'),
    path('export_3/pngbl/', views.e_datapengembalian, name='e_datapengembalian'),
    path('export_4/rqst/', views.e_request, name='e_request'),
    path('tambahsiswa/', views.tambahsiswa, name='tambahsiswa'),
    path('t_kelompok/', views.t_kelompok, name='t_kelompok'),
    path('t_kelas/', views.t_kelas, name='t_kelas'),
    path('kls/hapus/<int:id_kelas>', views.h_kelas, name='h_kelas'),
    path('d_pengunjung/', views.d_pengunjung, name='d_pengunjung'),
    path('data/hapus/<int:id_pengunjung>',
         views.h_pengunjung, name='h_pengunjung'),

    # url siswa
    path('petugas', views.petugas, name='petugas'),
    path('databuku/', views.databuku, name='databuku'),
    path('data/show/<int:id_buku>', views.show, name='show'),
    path('pinjam', views.pinjam, name='pinjam'),
    path('pengembalian/', views.pengembalian, name='pengembalian'),
    path('profile/', views.profile, name='profile'),
    path('request/', views.request, name='request'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
