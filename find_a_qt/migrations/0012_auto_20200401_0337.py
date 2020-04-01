# Generated by Django 3.0.4 on 2020-04-01 03:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('find_a_qt', '0011_auto_20200401_0250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(upload_to='question_images/'),
        ),
        migrations.AlterField(
            model_name='question',
            name='session_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 1, 3, 37, 21, 703835, tzinfo=utc)),
        ),
    ]