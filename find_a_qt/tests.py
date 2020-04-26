from django.test import TestCase
from .models import Question, Answer
from users.models import Profile
from .models import Question, Answer
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db import IntegrityError
from django.conf import settings
from .forms import QuestionForm, AnswerForm, RoomForm
from chat.models import Room
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


# class AnswerStrTestCase(TestCase):
#     def setUp(self):
#         Question.objects.create(body="What is life?", class_name ="PHIL 1710", author_name = 'Josh', topic = 'CS')
#         Question.objects.create(body="What is 9+10?", class_name ="MATH 101", author_name = 'Drake', topic = 'MATH')
#         Question.objects.create(body="How do I do 3240?", class_name ="CS 3240", author_name = 'FindaQT', topic = 'CS')
#         Answer.objects.create(text ="Life is fun", post_id = 1)
#         Answer.objects.create(text ="9+10 = 19", post_id = 1)
#         Answer.objects.create(text ="You just use Django and start coding buddy", post_id = 1)

#     def test_str(self):
#         response = self.client.get('/answers/')
#         response1 = self.client.get('/questions/')
#         print(response1)
#         self.assertContains(response, 'Life is fun')
#         self.assertContains(response, '9+10 = 19')
#         self.assertContains(response, 'You just use Django and start coding buddy')


class QuestionFormTest(TestCase):
    def setUp(self):
        q1 = Question.objects.create(body="What is life?", class_name ="PHIL 1710", author_name = 'Josh', topic = 'Computer Science', urgency = 'No rush')

    def test_form_true(self):
        w = Question.objects.get(body="What is life?")
        data = {'body': w.body, 'class_name': w.class_name, 'class_name': w.class_name, 'author_name': w.author_name, 'topic': w.topic, 'urgency':w.urgency}
        form = QuestionForm(data=data)
        self.assertTrue(form.is_valid())

    def test_form_false(self):
        w = Question.objects.get(body="What is life?")
        data = {'body': w.body, 'author_name': w.author_name, 'topic': w.topic, 'urgency':w.urgency}
        form = QuestionForm(data=data)
        self.assertFalse(form.is_valid())



class RoomFormTest(TestCase):
    def setUp(self):
        r1 = Room.objects.create(name = 'STAT2120', slug ='STAT-2120' , description = "Chat for STAT 2120 students")

    def test_form_true(self):
        w = Room.objects.get(name="STAT2120")
        data = {'name': w.name, 'slug': w.slug, 'description': w.description, }
        form = RoomForm(data=data)
        self.assertTrue(form.is_valid())

    def test_form_false(self):
        w = Room.objects.get(name="STAT2120")
        data = { 'slug': w.slug, 'description': w.description, }
        form = RoomForm(data=data)
        self.assertFalse(form.is_valid())


class AnswerPostTest(TestCase):
     def test_str(self):
        q1 = Question.objects.create(body="What is life?", class_name ="PHIL 1710", author_name = 'Josh', topic = 'Computer Science', urgency = 'No rush')
        q2 = Question.objects.create(body="What isn't life?", class_name ="PHIL 1710", author_name = 'Josh', topic = 'Computer Science', urgency = 'No rush')
        a1 = Answer.objects.create(post=q1, text ="Google", author_name = 'Josh')
        a2 = Answer.objects.create(post=q2, text ="Google", author_name = 'Josh')
        self.assertEqual(a1.post, q1)
        self.assertEqual(a2.post, q2)

# class AnswerFormTest(TestCase):
#     def test_form_true(self):
#         sq1 = Question.objects.create(body="What is life?", class_name ="PHIL 1710", author_name = 'Josh', topic = 'Computer Science', urgency = 'No rush')
#         a1 = Answer.objects.create(post=sq1, text ="Google", author_name = 'Josh')
#         data = {'post': sq1, 'text': a1.text}
#         form = AnswerForm(data=data)
#         self.assertTrue(form.is_valid())

#     def test_form_false(self):
#         sq1 = Question.objects.create(body="What is life?", class_name ="PHIL 1710", author_name = 'Josh', topic = 'Computer Science', urgency = 'No rush')
#         a1 = Answer.objects.create(post=sq1, text ="Google", author_name = 'Josh')
#         data = {'text': a1.text}
#         form = AnswerForm(data=data)
#         self.assertFalse(form.is_valid())

class AnswerQuestionRelatedTests(TestCase):
    def setUp(self):
        q1 = Question.objects.create(body="What is life?", class_name ="PHIL 1710", author_name = 'Josh', topic = 'Computer Science', urgency = 'No rush')
        a1 = Answer.objects.create(post=q1, text ="Google", author_name = 'Josh')
    def relatedmodelset(self):
        q1 = Question.objects.get(body="What is life?")
        answer_set = q1.answer.all()
        A1 = Answer.objects.get(text ="Google")
        self.assertEqual(answer_set[0], A1)

class AnswerQuestionRelatedTestsMultiple(TestCase):
    def setUp(self):
        q1 = Question.objects.create(body="What is life?", class_name ="PHIL 1710", author_name = 'Josh', topic = 'Computer Science', urgency = 'No rush')
        a1 = Answer.objects.create(post=q1, text ="Google", author_name = 'Josh')
        a2 = Answer.objects.create(post=q1, text ="Chegg", author_name = 'Josh')
    def relatedmodelset(self):
        q1 = Question.objects.get(body="What is life?")
        answer_set = q1.answer.all()
        A1 = Answer.objects.get(text ="Google")
        A2 = Answer.objects.get(text ="Chegg")
        self.assertEqual(answer_set[0], A1)
        self.assertEqual(answer_set[1], A2)


