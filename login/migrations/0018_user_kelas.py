# Generated by Django 3.2.12 on 2022-03-07 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0017_delete_notifikasi'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='kelas',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
