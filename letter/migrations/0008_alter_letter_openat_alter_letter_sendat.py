# Generated by Django 4.1.4 on 2022-12-31 09:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letter', '0007_remove_letter_dday_alter_letter_openat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='openAt',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 30, 15, 0, 0, 918669, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='letter',
            name='sendAt',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 31, 9, 16, 11, 918669, tzinfo=datetime.timezone.utc)),
        ),
    ]
