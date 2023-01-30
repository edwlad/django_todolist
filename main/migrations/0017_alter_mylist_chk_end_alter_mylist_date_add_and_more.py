# Generated by Django 4.1.5 on 2023-01-28 05:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_mylist_chk_end_alter_mylist_date_add_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mylist',
            name='chk_end',
            field=models.BooleanField(default=False, help_text='Завершить', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='mylist',
            name='date_add',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='Дата создания задачи', verbose_name='Создано'),
        ),
        migrations.AlterField(
            model_name='mylist',
            name='date_end',
            field=models.DateTimeField(blank=True, default=None, help_text='Дата завершения задачи', null=True, verbose_name='Завершено'),
        ),
    ]