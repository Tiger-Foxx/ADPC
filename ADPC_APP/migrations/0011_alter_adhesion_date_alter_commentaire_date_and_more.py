# Generated by Django 5.0.3 on 2024-03-09 15:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ADPC_APP', '0010_alter_adhesion_date_alter_commentaire_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adhesion',
            name='date',
            field=models.DateField(auto_created=True, default=datetime.datetime(2024, 3, 9, 16, 48, 45, 636536), editable=False),
        ),
        migrations.AlterField(
            model_name='commentaire',
            name='date',
            field=models.DateField(auto_created=True, default=datetime.datetime(2024, 3, 9, 16, 48, 45, 634492), editable=False),
        ),
        migrations.AlterField(
            model_name='don',
            name='date',
            field=models.DateField(auto_created=True, default=datetime.datetime(2024, 3, 9, 16, 48, 45, 635536), editable=False),
        ),
    ]
