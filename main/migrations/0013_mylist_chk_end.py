# Generated by Django 4.1.5 on 2023-01-27 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0012_alter_mylist_date_add"),
    ]

    operations = [
        migrations.AddField(
            model_name="mylist",
            name="chk_end",
            field=models.BooleanField(default=False, help_text="Задача завершена"),
        ),
    ]
