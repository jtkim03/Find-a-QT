from django.test import TestCase
from .models import Tutor, Student

class TutorTestCase(TestCase):
    def setUp(self):
        Tutor.objects.create(first_name="John", last_name="Doe", phone_number = '+14124839124', major = 'CS', year_in_school = 'FR')
        #Animal.objects.create(name="cat", sound="meow")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        John = Tutor.objects.get(first_name="John")
        self.assertEqual(str(John), 'John Doe')


class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(first_name="Jane", last_name="Doe", phone_number = '+14134839124', major = 'CS', year_in_school = 'SR')
        #Animal.objects.create(name="cat", sound="meow")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        Jane = Student.objects.get(first_name="Jane")
        self.assertEqual(str(Jane), 'Jane Doe')