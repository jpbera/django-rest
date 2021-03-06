# Generated by Django 3.2 on 2021-05-23 11:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empManagement', '0007_alter_clientdatacapture_created_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Client_ID')),
                ('client_name', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'Client',
                'db_table': 'Client',
            },
        ),
        migrations.AlterField(
            model_name='clientdatacapture',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 23, 17, 20, 32, 767552)),
        ),
    ]
