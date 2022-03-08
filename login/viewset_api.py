from login.models import Buku
from login.serializers import BukuSerializer
from rest_framework import viewsets


class Bukuviewset(viewsets.ModelViewSet):
    queryset = Buku.objects.all()
    serializer_class = BukuSerializer
