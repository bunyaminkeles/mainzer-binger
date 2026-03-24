from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteZiyaret',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toplam', models.PositiveBigIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Site Ziyareti',
            },
        ),
    ]
