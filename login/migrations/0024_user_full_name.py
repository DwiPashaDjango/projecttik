# Generated by Django 3.2.12 on 2022-03-20 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0023_pengunjung'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
