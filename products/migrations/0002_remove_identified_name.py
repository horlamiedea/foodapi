# Generated by Django 3.1 on 2022-05-04 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='identified',
            name='name',
        ),
    ]
