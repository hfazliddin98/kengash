# Generated by Django 4.2.7 on 2023-12-16 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ovoz', '0009_remove_statistika_elon_statistika_taklif_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statistika',
            old_name='betaraf',
            new_name='betaraflar',
        ),
        migrations.RenameField(
            model_name='statistika',
            old_name='qatnashmagan',
            new_name='qatnashmaganlar',
        ),
    ]
