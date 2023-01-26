# Generated by Django 4.1.5 on 2023-01-26 12:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mylist',
            name='date_add',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 26, 19, 47, 42, 844894), help_text='Дата создания задачи'),
        ),
        migrations.AlterField(
            model_name='mylist',
            name='date_end',
            field=models.DateTimeField(blank=True, default=None, help_text='Дата выполнения задачи', null=True),
        ),
    ]
