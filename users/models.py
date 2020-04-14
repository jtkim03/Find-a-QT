from django.db import models
from django.contrib.auth.models import User
from find_a_qt.models import Student,Tutor
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver
import statistics as stats

class Profile(models.Model):
    UNDECIDED = 'Undecided'
    ASTRONOMY = 'Astronomy'
    BIOLOGY = 'Biology'
    CHEMISTRY = 'Chemistry'
    COMPUTER_SCIENCE = 'Computer Science'
    ENGINEERING = 'Engineering'
    EARTH_SCIENCES = 'Earth Sciences'
    HEALTH_SCIENCES = 'Health Sciences'
    INFORMATION_TECHNOLOGY = 'Information Technology'
    MATHEMATICS = 'Mathematics'
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
    FRESHMAN = 'First Year'
    SOPHOMORE = 'Second Year'
    JUNIOR = 'Third Year'
    SENIOR = 'Fourth Year'
    GRADUATE = 'Graduate Student'
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, 'First'),
        (SOPHOMORE, 'Second'),
        (JUNIOR, 'Third'),
        (SENIOR, 'Fourth'),
        (GRADUATE, 'Grad Student'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    bio = models.TextField(default='', blank=True)
    major = models.CharField(max_length=30,
                             choices=MAJOR_CHOICES,
                             default=UNDECIDED,
                             blank=True)
    year_in_school = models.CharField(max_length=30,
                                      choices=YEAR_IN_SCHOOL_CHOICES,
                                      default=FRESHMAN,
                                      blank=True)


    def __str__(self):
        return f"{self.user.username}'s Profile"

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Like(models.Model):
    ''' like  user '''

    users = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    profiles = models.ForeignKey(Profile, on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


"""class DisLike(models.Model):
    ''' Dislike  user '''

    profile = models.OneToOneField(Profile, related_name="dis_likes", on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='requirement_comment_dis_likes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.profile.name)[:30]"""
