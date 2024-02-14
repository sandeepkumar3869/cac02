# Generated by Django 5.0.2 on 2024-02-14 12:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bottomlevel', '0006_user_alter_bottomlevel_task_created_on'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='DefaultName', max_length=255),
        ),
        migrations.AlterField(
            model_name='bottomlevel',
            name='task_created_on',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 14, 18, 22, 10, 349958)),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=255),
        ),
    ]
