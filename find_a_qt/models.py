from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User

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
UNDECIDED = 'Undecided'
ASTRONOMY = 'Astronomy'
BIOLOGY = 'Biology'
CHEMISTRY = 'Chemistry'
COMPUTER_SCIENCE = 'Computer Science'
ENGINEERING = 'Engineering'
EARTH_SCIENCES = 'Earth Sciences'
HEALTH_SCIENCES = 'Health Sciences'
INFORMATION_TECHNOLOGY = 'Information Technology'
MATHEMATICS = 'Math'
PHYSICS = 'Physics'
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
NOW = 'Due immediately'
LATER = 'Due within a week'
WHENEVER = 'No rush'
URGENT_CHOICES = [
    (NOW, 'Due immediately'),
    (LATER, 'Due within a week'),
    (WHENEVER, 'No rush'),
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
    time_submission = models.DateTimeField(auto_now=True)

    urgency = models.CharField(
        max_length=30,
        choices=URGENT_CHOICES,
        default=WHENEVER,
    )
    image = models.ImageField(upload_to='question_images/', blank = True)

    def get_absolute_url(self):
        return reverse('faqt-home')

    def __str__(self):
        return self.body

    def get_queryset(self):
        return Project.objects



class Answer(models.Model):
    class stars(models.IntegerChoices):
        One = 1
        Two = 2
        Three = 3
        Four = 4
        Five = 5
    post = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer', default=None)
    author_name = models.CharField(max_length=50, default = "Anonymous")
    text = models.TextField(max_length = 500)
    time_submission = models.DateTimeField(auto_now=True,)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    image = models.ImageField(upload_to='answer_images/', blank = True, default=None)
    #questionid

    def add_upvote(self):
        self.upvotes += 1

    def add_downvote(self):
        self.downvotes += 1

    def __str__(self):
        return self.text

class Upvote(models.Model):
    answerID = models.ForeignKey(Answer, on_delete=models.CASCADE)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
