# Generated by Django 4.2.7 on 2023-12-19 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ovoz', '0011_alter_statistika_rasm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statistika',
            name='rasm',
        ),
    ]