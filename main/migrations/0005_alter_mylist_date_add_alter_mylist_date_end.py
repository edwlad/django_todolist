# Generated by Django 4.1.5 on 2023-01-26 14:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_mylist_date_add'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mylist',
            name='date_add',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2023, 1, 26, 21, 4, 30, 807478), help_text='Дата создания задачи'),
        ),
        migrations.AlterField(
            model_name='mylist',
            name='date_end',
            field=models.DateTimeField(blank=True, db_index=True, default=None, help_text='Дата выполнения задачи', null=True),
        ),
    ]