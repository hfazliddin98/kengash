# Generated by Django 4.2.7 on 2023-12-11 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ovoz', '0004_taklif_alter_baxo_elon_alter_statistika_elon_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taklif',
            name='rasm',
        ),
    ]
