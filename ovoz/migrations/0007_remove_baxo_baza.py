# Generated by Django 4.2.7 on 2023-12-13 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ovoz', '0006_rename_elon_baxo_taklif_id_baxo_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baxo',
            name='baza',
        ),
    ]