# Generated by Django 4.1.5 on 2023-01-26 12:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_mylist_date_add_alter_mylist_date_end'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mylist',
            name='date_add',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 26, 19, 54, 40, 240000), help_text='Дата создания задачи'),
        ),
    ]
