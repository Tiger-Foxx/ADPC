# Generated by Django 5.0.3 on 2024-03-08 09:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ADPC_APP', '0002_alter_adhesion_date_alter_commentaire_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Souvenir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripion', models.CharField(max_length=250)),
                ('lien', models.URLField(default='#')),
                ('date', models.DateField()),
                ('photo', models.ImageField(null=True, upload_to='imageSouvenirs')),
            ],
        ),
        migrations.AlterField(
            model_name='adhesion',
            name='date',
            field=models.DateField(auto_created=True, default=datetime.datetime(2024, 3, 8, 10, 26, 6, 584875), editable=False),
        ),
        migrations.AlterField(
            model_name='commentaire',
            name='date',
            field=models.DateField(auto_created=True, default=datetime.datetime(2024, 3, 8, 10, 26, 6, 582875), editable=False),
        ),
        migrations.AlterField(
            model_name='don',
            name='date',
            field=models.DateField(auto_created=True, default=datetime.datetime(2024, 3, 8, 10, 26, 6, 583875), editable=False),
        ),
    ]