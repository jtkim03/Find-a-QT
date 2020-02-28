from django.db import models
# hello world
# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField

class Student(models.Model):
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    GRADUATE = 'GR'
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (GRADUATE, 'Graduate'),
    ]
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )

    major = models.CharField(max_length=55)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    name = models.CharField(max_length=50)

class Tutor(models.Model):
    first_name_Tutor = models.CharField(max_length=50)
    last_name_Tutor = models.CharField(max_length=50)
    bio_Tutor = models.CharField(max_length=500)
    phone_number_Tutor = PhoneNumberField(blank=True) #https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models
    major_Tutor = models.CharField(max_length=50, null=True, blank=True) #Maybe change this to dynamic to add another major
    minor_Tutor = models.CharField(max_length=50, null=True, blank=True) #optional but also maybe change to make dynamic so that only need to add this field if person has a minor
    year_Tutor =  models.IntegerField(blank=True, null=True) #Let this only be an ineteger
    number_tutored = 0 #This should be incremented everytime the tutor has tutored a new student

    def __str__(self):
        return self.first_name_Tutor + ' ' + self.last_name_Tutor
