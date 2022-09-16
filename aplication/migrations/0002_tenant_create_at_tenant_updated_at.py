# Generated by Django 4.1 on 2022-08-30 13:21

import aplication.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenant',
            name='create_at',
            field=models.DateField(auto_created=True, default=aplication.models.get_default_date),
        ),
        migrations.AddField(
            model_name='tenant',
            name='updated_at',
            field=models.DateField(auto_created=True, null=True),
        ),
    ]