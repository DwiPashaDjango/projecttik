# Generated by Django 3.2.12 on 2022-03-06 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0013_alter_request_nama'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pengembalian',
            name='tanggal',
            field=models.DateField(auto_now_add=True, max_length=40),
        ),
    ]