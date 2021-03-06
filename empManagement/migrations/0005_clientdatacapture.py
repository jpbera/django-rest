# Generated by Django 3.2 on 2021-05-22 17:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empManagement', '0004_todo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientDataCapture',
            fields=[
                ('Capture_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Capture_id')),
                ('client_name', models.CharField(blank=True, max_length=500, null=True)),
                ('client_system_name', models.CharField(blank=True, max_length=500, null=True)),
                ('session_id', models.CharField(blank=True, max_length=500, null=True)),
                ('status_code', models.CharField(blank=True, max_length=500, null=True)),
                ('response_message', models.CharField(blank=True, max_length=500, null=True)),
                ('row_count', models.IntegerField(blank=True, null=True)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2021, 5, 22, 22, 41, 52, 434736))),
            ],
            options={
                'verbose_name': 'ClientDataCapture',
                'db_table': 'ClientDataCapture',
            },
        ),
    ]
