# Generated by Django 3.2.12 on 2022-02-27 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_buku_kelompok'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buku',
            name='jumlah_id',
        ),
    ]
