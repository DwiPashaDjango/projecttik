# Generated by Django 3.2.12 on 2022-02-27 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_buku'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kelompok',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.TextField()),
            ],
        ),
    ]
