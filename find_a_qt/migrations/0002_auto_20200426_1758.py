# Generated by Django 3.0.3 on 2020-04-26 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('find_a_qt', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='session_date',
        ),
        migrations.RemoveField(
            model_name='question',
            name='session_time',
        ),
    ]
