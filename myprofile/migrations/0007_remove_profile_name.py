# Generated by Django 4.2.11 on 2024-03-11 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0006_profile_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
    ]
