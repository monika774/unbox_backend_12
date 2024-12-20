# Generated by Django 5.1.3 on 2024-11-30 12:20

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unbox_speed_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpeedData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speed', models.FloatField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'Speed Data',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.DeleteModel(
            name='Speed_Detail',
        ),
    ]
