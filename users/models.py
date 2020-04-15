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
    users = models.ManyToManyField(User, related_name='like_set')
    current_user = models.ForeignKey(User, related_name='like_owner', on_delete=models.CASCADE, null=True)

    @classmethod
    def give_like(cls, current_user, new_like):
        like, created = cls.objects.get_or_create(
            current_user=current_user
        )
        like.users.add(new_like)
        dislike, created = Dislike.objects.get_or_create(
            current_user=current_user
        )
        dislike.users.remove(new_like)

    @classmethod
    def get_num_likes(cls, current_user):
        sum = 0
        for i in cls.objects.all():
            for j in i.users.all():
                if current_user == j:
                    sum += 1

        return sum


    def __str__(self):
        return str(self.current_user) \
               + " is liked by " \
               + str(self.get_num_likes(self.current_user)) + " users!"

class Dislike(models.Model):
    users = models.ManyToManyField(User, related_name='dislike_set')
    current_user = models.ForeignKey(User, related_name='dislike_owner', on_delete=models.CASCADE, null=True)

    @classmethod
    def give_dislike(cls, current_user, new_dislike):
        dislike, created = cls.objects.get_or_create(
            current_user=current_user
        )
        dislike.users.add(new_dislike)
        like, created = Like.objects.get_or_create(
            current_user=current_user
        )
        like.users.remove(new_dislike)


    @classmethod
    def get_num_dislikes(cls, current_user):
        sum = 0
        for i in cls.objects.all():
            for j in i.users.all():
                if current_user == j:
                    sum += 1
        return sum

    def __str__(self):
        return str(self.current_user) \
               + " is disliked by " \
               + str(self.get_num_dislikes(self.current_user)) + " users!"
