# Generated by Django 5.0.3 on 2024-03-09 16:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ADPC_APP', '0015_alter_adhesion_date_alter_commentaire_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adhesion',
            name='date',
            field=models.DateField(auto_created=True, default=datetime.datetime(2024, 3, 9, 17, 1, 30, 312667), editable=False),
        ),
        migrations.AlterField(
            model_name='commentaire',
            name='date',
            field=models.DateField(auto_created=True, default=datetime.datetime(2024, 3, 9, 17, 1, 30, 308963), editable=False),
        ),
        migrations.AlterField(
            model_name='don',
            name='date',
            field=models.DateField(auto_created=True, default=datetime.datetime(2024, 3, 9, 17, 1, 30, 310609), editable=False),
        ),
    ]
