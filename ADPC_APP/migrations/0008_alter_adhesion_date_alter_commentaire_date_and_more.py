# Generated by Django 5.0.3 on 2024-03-09 15:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ADPC_APP', '0007_alter_adhesion_date_alter_commentaire_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adhesion',
            name='date',
            field=models.DateField(auto_created=True, default=datetime.datetime(2024, 3, 9, 16, 30, 46, 840763), editable=False),
        ),
        migrations.AlterField(
            model_name='commentaire',
            name='date',
            field=models.DateField(auto_created=True, default=datetime.datetime(2024, 3, 9, 16, 30, 46, 839737), editable=False),
        ),
        migrations.AlterField(
            model_name='don',
            name='NomDonneur',
            field=models.CharField(default='Inconnu', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='don',
            name='date',
            field=models.DateField(auto_created=True, default=datetime.datetime(2024, 3, 9, 16, 30, 46, 839737), editable=False),
        ),
        migrations.AlterField(
            model_name='don',
            name='telephone',
            field=models.CharField(default='Inconnu', max_length=13, null=True),
        ),
    ]
