# Generated by Django 3.0.3 on 2020-04-14 21:08

import datetime
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('topic', models.CharField(choices=[('Undecided', 'Undecided'), ('Astronomy', 'Astronomy'), ('Biology', 'Biology'), ('Chemistry', 'Chemistry'), ('Computer Science', 'Computer Science'), ('Engineering', 'Engineering'), ('Earth Sciences', 'Earth Sciences'), ('Health Sciences', 'Health Sciences'), ('Information Technology', 'Information Technology'), ('Math', 'Mathematics'), ('Physics', 'Physics')], default='Undecided', max_length=30)),
                ('class_name', models.CharField(default='', max_length=50)),
                ('author_name', models.CharField(default='Anonymous', max_length=50)),
                ('session_date', models.DateField(default=datetime.datetime.now)),
                ('session_time', models.TimeField(default=datetime.datetime.now)),
                ('time_submission', models.DateTimeField(auto_now=True)),
                ('urgency', models.CharField(choices=[('Due immediately', 'Due immediately'), ('Due within a week', 'Due within a week'), ('No rush', 'No rush')], default='No rush', max_length=30)),
                ('image', models.ImageField(blank=True, upload_to='question_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_in_school', models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate')], default='FR', max_length=2)),
                ('major', models.CharField(choices=[('Undecided', 'Undecided'), ('Astronomy', 'Astronomy'), ('Biology', 'Biology'), ('Chemistry', 'Chemistry'), ('Computer Science', 'Computer Science'), ('Engineering', 'Engineering'), ('Earth Sciences', 'Earth Sciences'), ('Health Sciences', 'Health Sciences'), ('Information Technology', 'Information Technology'), ('Math', 'Mathematics'), ('Physics', 'Physics')], default='Undecided', max_length=30)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_in_school', models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate')], default='FR', max_length=2)),
                ('major', models.CharField(choices=[('Undecided', 'Undecided'), ('Astronomy', 'Astronomy'), ('Biology', 'Biology'), ('Chemistry', 'Chemistry'), ('Computer Science', 'Computer Science'), ('Engineering', 'Engineering'), ('Earth Sciences', 'Earth Sciences'), ('Health Sciences', 'Health Sciences'), ('Information Technology', 'Information Technology'), ('Math', 'Mathematics'), ('Physics', 'Physics')], default='Undecided', max_length=30)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('number_tutored', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(default='Anonymous', max_length=50)),
                ('text', models.TextField(max_length=500)),
                ('time_submission', models.DateTimeField(auto_now=True)),
                ('upvotes', models.IntegerField(default=0)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='find_a_qt.Question')),
            ],
        ),
    ]
