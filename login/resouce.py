from import_export import resources
from login.models import Buku, Pengembalian, Pinjam, Request
from import_export.fields import Field


class Bukuresouce(resources.ModelResource):
    kelompok_id__nama = Field(attribute='kelompok_id__nama',
                              column_name='kelompok_buku')

    class Meta:
        model = Buku
        fields = ['judul', 'tanggal',
                  'kelompok_id__nama', 'penulis', 'penerbit', 'jumlah']
        export_order = ['judul', 'penulis', 'penerbit',
                        'kelompok_id__nama', 'jumlah', 'tanggal']


class Export_datapeminjam(resources.ModelResource):
    class Meta:
        model = Pinjam
        fields = ['judul', 'nama', 'kelas', 'tanggal', 't_pengembalian']


class Export_datapengembalian(resources.ModelResource):
    judul = Field(attribute='judul', column_name='judul_buku')
    nama = Field(attribute='nama', column_name='nama_siswa')
    tanggal = Field(attribute='tanggal', column_name='tanggal-pengembalian')

    class Meta:
        model = Pengembalian
        fields = ['nama', 'judul', 'kelas', 'tanggal']
        export_order = ['nama', 'judul', 'kelas', 'tanggal']


class Export_datarequest(resources.ModelResource):
    judul = Field(attribute='judul', column_name='judul_buku')
    nama = Field(attribute='nama', column_name='nama_siswa')

    class Meta:
        model = Request
        fields = ['nama', 'judul', 'kelas', 'tanggal']
        export_order = ['nama', 'judul', 'kelas', 'tanggal']
