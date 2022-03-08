from dataclasses import fields
from login.models import Buku
from rest_framework import serializers


class BukuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buku
        fields = ['id', 'judul', 'penulis', 'penerbit']
