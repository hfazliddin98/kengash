# Generated by Django 4.2.7 on 2023-11-29 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_davomat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='davomat',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]
