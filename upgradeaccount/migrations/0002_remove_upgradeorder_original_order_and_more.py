# Generated by Django 4.2.11 on 2024-04-07 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upgradeaccount', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upgradeorder',
            name='original_order',
        ),
        migrations.AlterField(
            model_name='upgradeorder',
            name='order_number',
            field=models.UUIDField(editable=False),
        ),
    ]
