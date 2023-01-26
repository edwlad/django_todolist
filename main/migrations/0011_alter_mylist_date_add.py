# Generated by Django 4.1.5 on 2023-01-26 14:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_mylist_date_add'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mylist',
            name='date_add',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2023, 1, 26, 21, 57, 28, 695453), help_text='Дата создания задачи'),
        ),
    ]