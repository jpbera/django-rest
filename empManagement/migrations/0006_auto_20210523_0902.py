# Generated by Django 3.2 on 2021-05-23 03:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empManagement', '0005_clientdatacapture'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientdatacapture',
            name='action',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='clientdatacapture',
            name='method_name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='clientdatacapture',
            name='parameter',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='clientdatacapture',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 23, 9, 2, 32, 440621)),
        ),
    ]
