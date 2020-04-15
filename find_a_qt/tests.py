from django.test import TestCase
from .models import Question
from users.models import Profile
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db import IntegrityError
from django.conf import settings
import os 

class QuestionStrTestCase(TestCase):
    def setUp(self):
        Question.objects.create(body="What is life?", class_name ="PHIL 1710", author_name = 'Josh', topic = 'CS')

    def test_str(self):
        """Str returns the correct value (first and last name)"""
        Q1 = Question.objects.get(body="What is life?")
        self.assertEqual(str(Q1), 'What is life?')

''' Commented because it creates a new photo everytime in question_images without  way to automatically delete it after the test
class QuestionPhotoTestCase(TestCase):
    def setUp(self):
        question = Question.objects.create(body="Image Test", class_name ="ASTR 1710", author_name = 'Josh', topic = 'ASTR',
        image = SimpleUploadedFile(name='croppedlogo.png', content=open('find_a_qt/static/find_a_qt/images/croppedlogo.png', 'rb').read(), content_type='image/jpeg'))
    def test_str(self):
        self.assertEqual(Question.objects.count(), 1)
'''

class QuestionIndexTest(TestCase):
    def setUp(self):
        Question.objects.create(body="What is life?", class_name ="PHIL 1710", author_name = 'Josh', topic = 'CS')
        Question.objects.create(body="What is 9+10?", class_name ="MATH 101", author_name = 'Drake', topic = 'MATH')
        Question.objects.create(body="How do I do 3240?", class_name ="CS 3240", author_name = 'FindaQT', topic = 'CS')

    def test_str(self):
        response = self.client.get('/questions/')
        self.assertContains(response, 'What is life?')
        self.assertContains(response, 'What is 9+10?')
        self.assertContains(response, 'How do I do 3240?')

class ProfileStrTestCase(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user('JohnD', 'johnd@mail.com', 'johnpassword')

    def test_str(self):
        test_user = self.test_user
        test_profile = Profile.objects.get(user=test_user)
        self.assertEqual(str(test_profile), "JohnD's Profile")

class UserCreationFailCase(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user('JohnD', 'johnd@mail.com', 'johnpassword')

    def test_str(self):
        try:
            self.test_user2 = User.objects.create_user('JohnD', 'johnd@mail.com', 'johnpassword')
        except:
            self.assertRaises(AttributeError)