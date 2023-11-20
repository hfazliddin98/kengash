# Generated by Django 4.2.7 on 2023-11-20 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Elon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('rasm', models.ImageField(blank=True, upload_to='nomzod/')),
                ('nomzod', models.CharField(max_length=255)),
                ('sana', models.DateField(auto_now_add=True)),
                ('vaqt', models.IntegerField(blank=True)),
                ('yoqish', models.BooleanField(default=False)),
                ('ovoz', models.CharField(blank=True, max_length=100)),
                ('baza', models.CharField(default='0', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Statistika',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rozilar', models.IntegerField(default=0)),
                ('qarshilar', models.IntegerField(default=0)),
                ('betaraf', models.IntegerField(default=0)),
                ('rasm', models.ImageField(upload_to='statistika/')),
                ('elon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ovoz.elon')),
            ],
        ),
        migrations.CreateModel(
            name='Baxo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baxo', models.CharField(max_length=200)),
                ('baza', models.CharField(default='0', max_length=10)),
                ('elon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ovoz.elon')),
            ],
        ),
    ]
