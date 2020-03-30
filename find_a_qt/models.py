from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse

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
UNDECIDED = 'UNDE'
ASTRONOMY = 'ASTR'
BIOLOGY = 'BIO'
CHEMISTRY = 'CHEM'
COMPUTER_SCIENCE = 'CS'
ENGINEERING = 'ENGR'
EARTH_SCIENCES = 'ES'
HEALTH_SCIENCES = 'HS'
INFORMATION_TECHNOLOGY = 'IT'
MATHEMATICS = 'MATH'
PHYSICS = 'PHYS'
MAJOR_CHOICES = [
    (UNDECIDED, 'Undecided'),
    (ASTRONOMY, 'Astronomy'),
    (BIOLOGY, 'Biology'),
    (CHEMISTRY, 'Chemistry'),
    (COMPUTER_SCIENCE, 'Computer Science'),
    (ENGINEERING, 'Engineering'),
    (EARTH_SCIENCES, 'Earth Sciences'),
    (HEALTH_SCIENCES, 'Health Sciences'),
    (INFORMATION_TECHNOLOGY, 'Information Technology'),
    (MATHEMATICS, 'Mathematics'),
    (PHYSICS, 'Physics'),
]


class Student(models.Model):
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )

    major = models.CharField(
        max_length = 30,
        choices = MAJOR_CHOICES,
        default = UNDECIDED,
    )
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


    def __str__(self):
        return self.last_name

class Tutor(models.Model):
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )
    #tutor_img = models.ImageField(upload_to='templates/find_a_qt/images/') 
    major = models.CharField(
        max_length = 30,
        choices = MAJOR_CHOICES,
        default = UNDECIDED,
    )

    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    #bio = models.CharField(max_length=100, default='Hey! I am using Find a QT!')

    number_tutored =  models.IntegerField(default = 0) #This should be incremented everytime the tutor has tutored a new student

    def __str__(self):
        return self.last_name


class Question(models.Model):
    body = models.TextField()

    topic = models.CharField(
        max_length = 30,
        choices = MAJOR_CHOICES,
        default = UNDECIDED,
    )

    class_name = models.CharField(max_length=50, default = "")
    author_name = models.CharField(max_length=50, default = "Anonymous")

    #date?
    #urgency
    #picture
    #topic??

    def get_absolute_url(self):
        return reverse('faqt-home')
<<<<<<< HEAD

    def __str__(self):
        return self.body
=======
>>>>>>> 07085f5a6c38d4a145ff94d1efbeb193143ce449


