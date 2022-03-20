from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Kelas, Pengembalian, Pinjam, Request, User, Buku, Kelompok


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Username'
            }
        )
    )
    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Full Name'
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Enter Email'
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Password'
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Repeat Password'
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',
                  'is_admin', 'is_siswa', 'kelas_id', 'full_name')


class Formbuku(forms.ModelForm):
    judul = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Judul Buku'
            }
        )
    )
    penulis = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Nama Penulis'
            }
        )
    )
    penerbit = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Penerbit'
            }
        )
    )
    jumlah = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Jumlah Buku'
            }
        )
    )
    keterangan = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control', 'placeholder': 'Keterangan Buku'
            }
        )
    )
    # kelompok_id = forms.CharField(
    #     widget=forms.Select(
    #         attrs={

    #         }
    #     )
    # )

    class Meta:
        model = Buku
        fields = ('judul', 'penulis', 'penerbit',
                  'jumlah', 'cover', 'kelompok_id', 'keterangan')
        export_order = [
            'judul', 'penulis', 'penerbit', 'jumlah', 'cover', 'kelompok_id__nama', 'keterangan'
        ]


class pinjamBuku(forms.ModelForm):
    judul = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Judul Buku'
            }
        )
    )
    nama = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Username'
            }
        )
    )
    kelas = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = Pinjam
        fields = ('judul', 'nama', 'kelas', 'tanggal', 't_pengembalian')


class pengembalianBuku(forms.ModelForm):
    nama = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Username'
            }
        )
    )
    judul = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'judul Buku'
            }
        )
    )
    kelas = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Kelas'
            }
        )
    )
    # tanggal = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control'
    #         }
    #     )
    # )

    class Meta:
        model = Pengembalian
        fields = ('nama', 'judul', 'kelas')


class Pre_order(forms.ModelForm):
    nama = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Username'
            }
        )
    )
    judul = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Judul Buku'
            }
        )
    )
    kelas = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Kelas'
            }
        )
    )

    class Meta:
        model = Request
        fields = ('nama', 'judul', 'kelas')


class Kelompokbuku(forms.ModelForm):
    nama = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Nama Kelompok Buku'
            }
        )
    )
    keterangan = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control', 'placeholder': 'Keterangan Buku'
            }
        )
    )

    class Meta:
        model = Kelompok
        fields = ['nama', 'keterangan']


class Tambahkelas(forms.ModelForm):
    kls = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Nama Kelas'
            }
        )
    )

    class Meta:
        model = Kelas
        fields = ['kls']
