# Generated by Django 5.0 on 2023-12-07 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='uloc',
        ),
    ]