# Generated by Django 4.2.7 on 2023-12-11 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ovoz', '0003_remove_elon_ovoz_elon_tugash'),
    ]

    operations = [
        migrations.CreateModel(
            name='Taklif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('rasm', models.ImageField(blank=True, upload_to='nomzod/')),
                ('nomzod', models.CharField(max_length=255)),
                ('vaqt', models.IntegerField(blank=True)),
                ('boshlanish_vaqti', models.CharField(blank=True, max_length=100)),
                ('tugash_vaqti', models.CharField(blank=True, max_length=100)),
                ('yoqish', models.BooleanField(default=False)),
                ('tugash', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='baxo',
            name='elon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ovoz.taklif'),
        ),
        migrations.AlterField(
            model_name='statistika',
            name='elon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ovoz.taklif'),
        ),
        migrations.DeleteModel(
            name='Elon',
        ),
    ]