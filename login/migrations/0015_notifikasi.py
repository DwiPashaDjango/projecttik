# Generated by Django 3.2.12 on 2022-03-06 12:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0014_alter_pengembalian_tanggal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notifikasi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keterangan', models.TextField(max_length=500)),
                ('tanggal', models.DateField(auto_now_add=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
