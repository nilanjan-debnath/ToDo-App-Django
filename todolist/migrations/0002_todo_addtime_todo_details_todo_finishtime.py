# Generated by Django 5.0.4 on 2024-04-23 09:16

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='addtime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='todo',
            name='details',
            field=models.CharField(default=None, max_length=1000),
        ),
        migrations.AddField(
            model_name='todo',
            name='finishtime',
            field=models.DateTimeField(default=None),
        ),
    ]
