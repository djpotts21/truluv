# Generated by Django 4.2.11 on 2024-03-11 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0004_profile_acceptnsfw_profile_ethnicity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
    ]
