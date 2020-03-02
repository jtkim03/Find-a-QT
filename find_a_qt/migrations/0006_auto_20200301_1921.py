# Generated by Django 3.0.3 on 2020-03-02 00:21

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('find_a_qt', '0005_auto_20200227_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='major',
            field=models.CharField(max_length=55),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True),
        ),
    ]
