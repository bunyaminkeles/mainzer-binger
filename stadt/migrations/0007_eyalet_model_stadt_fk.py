"""
Schema migration: Eyalet modeli eklendi, Stadt.eyalet FK bağlandı.
"""
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stadt', '0006_ayristry_mainz_bingen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eyalet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=100, verbose_name='Eyalet Adı')),
                ('slug', models.SlugField(unique=True, verbose_name='URL Slug')),
                ('kod', models.CharField(max_length=4, unique=True, verbose_name='Kısaltma (BY, NW…)')),
                ('baskent', models.CharField(blank=True, max_length=100, verbose_name='Başkent')),
                ('aktif', models.BooleanField(default=False, verbose_name='Aktif')),
            ],
            options={
                'verbose_name': 'Eyalet',
                'verbose_name_plural': 'Eyaletler',
                'ordering': ['ad'],
            },
        ),
        migrations.AddField(
            model_name='stadt',
            name='eyalet',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='sehirler',
                to='stadt.eyalet',
                verbose_name='Eyalet',
            ),
        ),
    ]
