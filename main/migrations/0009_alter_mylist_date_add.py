# Generated by Django 4.1.5 on 2023-01-26 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_mylist_date_add'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mylist',
            name='date_add',
            field=models.DateTimeField(auto_now=True, db_index=True, help_text='Дата создания задачи'),
        ),
    ]