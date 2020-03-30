from django.test import TestCase
from .models import Question
from users.models import Profile
from django.contrib.auth.models import User

#Tests whether the thing returned by the Student model under str is equal to what it should be
#class TutorStrTestCase(TestCase):
#    def setUp(self):
#        Tutor.objects.create(first_name="John", last_name="Doe", phone_number = '+14124839124', major = 'CS', year_in_school = 'FR')
#        #Tutor.objects.create(first_name="John", last_name="Doe", phone_number = '+14124839124', major = 'CS', year_in_school = 'FR')
#        #Animal.objects.create(name="cat", sound="meow")

#    def test_str(self):
#        """Str returns the correct value (first and last name)"""
#        John = Tutor.objects.get(first_name="John")
#        self.assertEqual(str(John), 'John Doe')


#Tests whether the thing returned by the Student model under str is equal to what it should be
'''
class StudentStrTestCase(TestCase):
    def setUp(self):
        Student.objects.create(first_name="Jane", last_name="Doe", phone_number = '+14134839124', major = 'CS', year_in_school = 'SR')

    def test_str(self):
        """Str returns the correct value (first and last name)"""
        Jane = Student.objects.get(first_name="Jane")
        self.assertEqual(str(Jane), 'Jane Doe')
'''

#Tests whether creating a new user with an already existing phone number creates an error
# class StudentClashNumber(TestCase):
#     def setUp(self):
#         Student.objects.create(first_name="Jane", last_name="Doe", phone_number = '+14134839124', major = 'CS', year_in_school = 'SR')

#     def test_error_ret(self):
#         """Str returns the correct value (first and last name)"""
#         Jane = Student.objects.get(first_name="Jane")
#         Student.objects.create(first_name="Jane", last_name="Doe", phone_number = '+14134839124', major = 'CS', year_in_school = 'SR')

class QuestionStrTestCase(TestCase):
    def setUp(self):
        Question.objects.create(body="What is life?", class_name ="PHIL 1710", author_name = 'MudBone', topic = 'CS')
        #Tutor.objects.create(first_name="John", last_name="Doe", phone_number = '+14124839124', major = 'CS', year_in_school = 'FR')
        #Animal.objects.create(name="cat", sound="meow")

    def test_str(self):
        """Str returns the correct value (first and last name)"""
        Q1 = Question.objects.get(body="What is life?")
        self.assertEqual(str(Q1), 'What is life?')


class ProfileStrTestCase(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user('JohnD', 'johnd@mail.com', 'johnpassword')


    def test_str(self):
        test_user = self.test_user
        test_profile = Profile.objects.get(user=test_user)
        self.assertEqual(str(test_profile), "JohnD's Profile")
