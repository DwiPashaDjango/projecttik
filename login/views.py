from django.shortcuts import render, redirect, HttpResponse
from .forms import Kelompokbuku, Pre_order, SignUpForm, LoginForm, Formbuku, Tambahkelas, pengembalianBuku, pinjamBuku
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Buku, Pengembalian, Pengunjung, Pinjam, Request, User, Kelas
from django.core.paginator import Paginator
from login.resouce import Bukuresouce, Export_datapeminjam, Export_datapengembalian, Export_datarequest
# Create your views here.


def daftar(request):
    judul = 'Perpustakaan Digital'
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun Berhasil Di Daftarkan')
            return redirect('login')
        else:
            messages.error(request, 'Gagal Mendaftarakan Akun')
            return redirect('daftar')
    else:
        form = SignUpForm()
    return render(request, 'login/register.html', {'form': form, 'msg': msg, 'jdl': judul})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    judul = 'Perpustakaan Digital'

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None and user.is_admin:
                login(request, user)
                messages.success(request, 'Berhasil Keluar')
                return redirect('home_admin')
            elif user is not None and user.is_siswa:
                login(request, user)
                messages.success(request, 'Berhasil Keluar')
                return redirect('petugas')
            else:
                messages.error(request, 'Akun Tidak Terdaftar')
                return redirect('login')
        else:
            messages.error(request, 'Validasi Akun Eror')
    return render(request, 'login/login.html', {'form': form, 'msg': msg, 'jdl': judul})


def home_admin(request):
    subJudul = 'Perpustakaan'
    judul = 'Dashboard'

    return render(request, 'admin/admin.html', {'jdl': judul, 'sb': subJudul})


def tambahPetugas(request):
    msg = None
    judul = 'Tambah Data Admin'
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Berhasil Menambahkan User')
            form.save()
            msg = 'user created'
            return redirect('tambahPetugas')
        else:
            messages.error(request, 'Gagal Menambahkan User')
            return redirect('tambahPetugas')
    else:
        form = SignUpForm()
    return render(request, 'admin/t_petugas.html', {'form': form, 'jdl': judul, 'msg': msg})


def tambahsiswa(request):
    msg = None
    judul = 'Tambah Data Siswa'
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Berhasil Menambahkan Siswa')
            form.save()
            msg = 'Siswa created'
            return redirect('tambahsiswa')
        else:
            messages.error(request, 'Gagal Gagal Menambahkan Siswa')
            return redirect('tambahsiswa')
    else:
        form = SignUpForm()
    return render(request, 'admin/t_siswa.html', {'form': form, 'jdl': judul})


def tambah_buku(request):
    judul = 'Tambah Data Buku'

    if request.POST:
        form = Formbuku(request.POST, request.FILES)
        if form.is_valid():
            messages.success(request, 'Berhasil Menambahkan Buku')
            form.save()
            form = Formbuku()
            return redirect('tambah_buku')
        else:
            messages.error(request, 'Gagal Menambahkan Buku')
            return redirect('tambah_buku')
    else:
        form = Formbuku()
    return render(request, 'admin/t_buku.html', {'form': form, 'jdl': judul})


def s_buku(request):
    judul = 'Data Buku'
    books = Buku.objects.all()

    p = Paginator(Buku.objects.all(), 5)
    page = request.GET.get('page')
    data = p.get_page(page)

    konteks = {
        'data': data,
        'jdl': judul,
        'books': books,
    }
    return render(request, 'admin/s_buku.html', konteks)


def ubah(request, id_buku):
    buku = Buku.objects.get(id=id_buku)
    tmp = 'admin/ubah-buku.html'

    if request.POST:
        form = Formbuku(request.POST, request.FILES, instance=buku)
        if form.is_valid():
            form.save()
            messages.success(request, 'Berhasil Mengubah Data Buku')
            return redirect('ubah', id_buku=id_buku)
        else:
            messages.error(request, 'Gagal Mengubah Data Buku')
            return redirect('ubah', id_buku=id_buku)
    else:
        form = Formbuku(instance=buku)
        konteks = {
            'jdl': 'Ubah Data Buku',
            'form': form,
            'buku': buku
        }
    return render(request, tmp, konteks)


def hapusbuku(request, id_buku):
    buku = Buku.objects.filter(id=id_buku)
    buku.delete()

    messages.success(request, 'Data Buku Berhasil Di Hapus')
    return redirect('s_buku')


def d_peminjam(request):
    tmp = 'admin/d_peminjam.html'
    pinjam = Pinjam.objects.all()

    p = Paginator(Pinjam.objects.all(), 5)
    page = request.GET.get('page')
    data = p.get_page(page)

    konteks = {
        'data': data,
        'pinjam': pinjam,
        'jdl': 'Data Peminjaman buku'
    }
    return render(request, tmp, konteks)


def hapus_p(request, id_peminjam):
    pinjam = Pinjam.objects.filter(id=id_peminjam)
    pinjam.delete()

    messages.success(request, 'Data Peminjam Berhasil Di Hapus')
    return redirect('d_peminjam')


def pengembalian_user(request):
    tmp = 'admin/d_pengembalian.html'
    pengembalian = Pengembalian.objects.all()

    p = Paginator(Pengembalian.objects.all(), 5)
    page = request.GET.get('page')
    data = p.get_page(page)

    konteks = {
        'data': data,
        'jdl': 'Data Pengembalian',
        'pngbl': pengembalian
    }
    return render(request, tmp, konteks)


def hapus_pngbl(request, id_pengembalian):
    pngbl = Pengembalian.objects.filter(id=id_pengembalian)
    pngbl.delete()

    messages.success(request, 'Data Pengembalian berhasil Di Hapus')
    return redirect('pengembalian_user')


def profile_admin(request):
    tmp = 'admin/profile/index.html'

    konteks = {
        'jdl': 'Profile'
    }
    return render(request, tmp, konteks)


def d_request(request):
    user = Request.objects.all()
    tmp = 'admin/request.html'

    p = Paginator(Request.objects.all(), 5)
    page = request.GET.get('page')
    data = p.get_page(page)

    konteks = {
        'data': data,
        'user': user,
        'jdl': 'Data Pre-order Buku Siswa'
    }
    return render(request, tmp, konteks)


def r_hapus(request, id_request):
    rqst = Request.objects.filter(id=id_request)
    rqst.delete()

    messages.success(request, 'Data Request Berhasil Di Hapus')
    return redirect('d_request')


def d_user(request):
    tmp = 'admin/d_user.html'
    user = User.objects.all()

    p = Paginator(User.objects.all(), 5)
    page = request.GET.get('page')
    data = p.get_page(page)

    konteks = {
        'data': data,
        'user': user,
        'jdl': 'Data User'
    }
    return render(request, tmp, konteks)


def u_hapus(request, id_user):
    user = User.objects.filter(id=id_user)
    user.delete()

    messages.success(request, 'Berhasil Di Hapus')
    return redirect('d_user')


def export_xls(request):
    buku = Bukuresouce()
    data = buku.export()
    response = HttpResponse(data.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="laporan data buku.xls"'
    return response


def e_datapeminjam(request):
    pmjm = Export_datapeminjam()
    data = pmjm.export()
    response = HttpResponse(data.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="laporan data Peminjam Buku.xls"'
    return response


def e_datapengembalian(request):
    pngbl = Export_datapengembalian()
    data = pngbl.export()
    response = HttpResponse(data.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="laporan data Pengembalian Buku.xls"'
    return response


def e_request(request):
    rqst = Export_datarequest()
    data = rqst.export()
    response = HttpResponse(data.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="laporan data Pre-order buku siswa.xls"'
    return response


def t_kelompok(request):
    judul = 'Tambah Kelompok Buku'

    if request.POST:
        form = Kelompokbuku(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Berhail Menambahkan Kelompok Buku')
            return redirect('t_kelompok')
        else:
            messages.error(request, 'Gagal Menambahkan Kelompok Buku')
            return redirect('t_kelompok')
    else:
        form = Kelompokbuku

        konteks = {
            'form': form,
            'jdl': judul,
        }
    return render(request, 'admin/t_kelompok.html', konteks)


def t_kelas(request):
    kls = Kelas.objects.all()

    p = Paginator(Kelas.objects.all(), 5)
    page = request.GET.get('page')
    data = p.get_page(page)

    if request.POST:
        form = Tambahkelas(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Berhasil menambahkan kelas')
            return redirect('t_kelas')
        else:
            messages.error(request, 'gagal menambahkan kelas')
            return redirect('t_kelas')
    else:
        form = Tambahkelas
        konteks = {
            'form': form,
            'data': data,
            'jdl': 'Tambah Kelas',
            'kls': kls,
        }
    return render(request, 'admin/t_kelas.html', konteks)


def h_kelas(request, id_kelas):
    kls = Kelas.objects.filter(id=id_kelas)
    kls.delete()

    messages.success(request, 'Berhasil Di Hapus')
    return redirect('t_kelas')


def d_pengunjung(request):
    tmp = 'admin/d_pengunjung.html'
    data = Pengunjung.objects.all()

    konteks = {
        'data': data,
        'jdl': 'Data Pengunjung',
    }
    return render(request, tmp, konteks)


def h_pengunjung(request, id_pengunjung):
    data = Pengunjung.objects.filter(id=id_pengunjung)
    data.delete()

    messages.success(request, 'Data berhasil Di Hapus')
    return redirect('d_pengunjung')
# page siswa


def petugas(request):
    buku = Buku.objects.all()
    p = Paginator(Buku.objects.all().order_by('?'), 3)
    page = request.GET.get('page')
    data = p.get_page(page)
    konteks = {
        'data': data,
        'buku': buku,
        'jdl': 'Home'
    }
    return render(request, 'petugas/index.html', konteks)


def databuku(request):
    p = Paginator(Buku.objects.all(), 5)
    page = request.GET.get('page')
    data = p.get_page(page)

    books = Buku.objects.all()
    konteks = {
        'books': books,
        'data': data,
        'jdl': 'Rak Buku'
    }
    return render(request, 'petugas/s_buku.html', konteks)


# def search_buku(request):
#     if request.POST:
#         keyword = request.POST['cari']
#         books = Buku.objects.filter(judul__contains=keyword)
#     else:
#         books = Buku.objects.all()
#     return render(request, 'petugas/s_buku.html', {'books': books})


def show(request, id_buku):
    data = Buku.objects.get(id=id_buku)

    konteks = {
        'data': data,
        'jdl': 'Detail buku'
    }
    return render(request, 'petugas/tampilan/index.html', konteks)


def pinjam(request):
    tmp = 'petugas/pinjam.html'

    if request.POST:
        form = pinjamBuku(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Berhasil Meminjam Buku')
            return redirect('pinjam')
        else:
            messages.error(request, 'Gagal Meminjam Buku')
            return redirect('pinjam')
    else:
        form = pinjamBuku()
        konteks = {
            'form': form,
            'jdl': 'Pinjam Buku'
        }
    return render(request, tmp, konteks)


def pengembalian(request):
    tmp = 'petugas/pengembalian.html'

    if request.POST:
        form = pengembalianBuku(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Berhasil Mengembalikan Buku')
            return redirect('pengembalian')
        else:
            messages.error(request, 'Gagal Mengembalikan Buku')
            return redirect('pengembalian')
    else:
        form = pengembalianBuku
        konteks = {
            'form': form,
            'jdl': 'Pengembalian Buku'
        }
    return render(request, tmp, konteks)


def profile(request):
    tmp = 'petugas/profile/index.html'

    konteks = {
        'jdl': 'Profile'
    }
    return render(request, tmp, konteks)


def request(request):
    tmp = 'petugas/request.html'

    if request.POST:
        form = Pre_order(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Berhasil Preorder Buku')
            return redirect('request')
        else:
            messages.error(request, 'Gagal Preorder Buku')
            return redirect('request')
    else:
        form = Pre_order()
        konteks = {
            'form': form,
            'jdl': 'Pre-Order Buku'
        }
    return render(request, tmp, konteks)
