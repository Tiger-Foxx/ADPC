# Generated by Django 5.0.3 on 2024-03-08 09:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ADPC_APP', '0003_souvenir_alter_adhesion_date_alter_commentaire_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adhesion',
            name='date',
            field=models.DateField(auto_created=True, default=datetime.datetime(2024, 3, 8, 10, 26, 40, 544106), editable=False),
        ),
        migrations.AlterField(
            model_name='commentaire',
            name='date',
            field=models.DateField(auto_created=True, default=datetime.datetime(2024, 3, 8, 10, 26, 40, 542111), editable=False),
        ),
        migrations.AlterField(
            model_name='don',
            name='date',
            field=models.DateField(auto_created=True, default=datetime.datetime(2024, 3, 8, 10, 26, 40, 543106), editable=False),
        ),
    ]