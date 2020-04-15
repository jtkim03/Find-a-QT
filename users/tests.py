from django.test import TestCase
from .models import Profile, Like, Dislike
from django.contrib.auth.models import User

# Create your tests here.

""" Tests if updating a Profile works correctly """
class ChangeProfileTest(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user('JohnD', 'johnd@mail.com', 'johnpassword')
    def test_str(self):
        test_user = self.test_user
        test_profile = Profile.objects.get(user=test_user)
        test_profile.bio = "I am a student at the University of Virginia"
        test_profile.save()
        self.assertEqual(test_profile.bio, "I am a student at the University of Virginia")

""" Tests the string function of the Like model """
class LikeStrTest(TestCase):
    def setUp(self):
        self.test_user_one = User.objects.create_user('JohnD', 'johnd@mail.com', 'johnpassword')
        self.test_user_two = User.objects.create_user('JoshD', 'joshd@mail.com', 'joshpassword')
    def test_str(self):
        test_user_one = self.test_user_one
        test_user_two = self.test_user_two
        test_like, created = Like.objects.get_or_create(current_user=test_user_one)
        test_like.users.add(test_user_two)
        test_like_dos, created = Like.objects.get_or_create(current_user=test_user_two)
        self.assertEqual(str(test_like_dos), "JoshD is liked by 1 users!")

""" Tests the give_like function of the Dislike model """
class GiveLikeTest(TestCase):
    def setUp(self):
        self.test_user_one = User.objects.create_user('JohnD', 'johnd@mail.com', 'johnpassword')
        self.test_user_two = User.objects.create_user('JoshD', 'joshd@mail.com', 'joshpassword')
    def test_str(self):
        test_user_one = self.test_user_one
        test_user_two = self.test_user_two
        Like.give_like(test_user_one, test_user_two)
        test_like, created = Like.objects.get_or_create(current_user=test_user_two)
        self.assertEqual(str(test_like), "JoshD is liked by 1 users!")

""" Tests the string function of the Dislike model """
class DislikeStrTest(TestCase):
    def setUp(self):
        self.test_user_one = User.objects.create_user('JohnD', 'johnd@mail.com', 'johnpassword')
        self.test_user_two = User.objects.create_user('JoshD', 'joshd@mail.com', 'joshpassword')
    def test_str(self):
        test_user_one = self.test_user_one
        test_user_two = self.test_user_two
        test_dislike, created = Dislike.objects.get_or_create(current_user=test_user_one)
        test_dislike.users.add(test_user_two)
        test_dislike_dos, created = Dislike.objects.get_or_create(current_user=test_user_two)
        self.assertEqual(str(test_dislike_dos), "JoshD is disliked by 1 users!")

""" Tests the give_dislike function of the Dislike model """
class GiveDislikeTest(TestCase):
    def setUp(self):
        self.test_user_one = User.objects.create_user('JohnD', 'johnd@mail.com', 'johnpassword')
        self.test_user_two = User.objects.create_user('JoshD', 'joshd@mail.com', 'joshpassword')
    def test_str(self):
        test_user_one = self.test_user_one
        test_user_two = self.test_user_two
        Dislike.give_dislike(test_user_one, test_user_two)
        test_dislike, created = Dislike.objects.get_or_create(current_user=test_user_two)
        self.assertEqual(str(test_dislike), "JoshD is disliked by 1 users!")

""" Tests after liking another User, if there had been a previous dislike from
    current user to the liked user, the dislike is removed."""
class RemoveDislikeIfLikeTest(TestCase):
    def setUp(self):
        self.test_user_one = User.objects.create_user('JohnD', 'johnd@mail.com', 'johnpassword')
        self.test_user_two = User.objects.create_user('JoshD', 'joshd@mail.com', 'joshpassword')
    def test_str(self):
        test_user_one = self.test_user_one
        test_user_two = self.test_user_two
        Dislike.give_dislike(test_user_one, test_user_two)
        Like.give_like(test_user_one, test_user_two)
        test_dislike, created = Dislike.objects.get_or_create(current_user=test_user_two)
        self.assertEqual(str(test_dislike), "JoshD is disliked by 0 users!")

""" Tests after disliking another User, if there had been a previous like from
    current user to the disliked user, the like is removed."""
class RemoveLikeIfDislikeTest(TestCase):
    def setUp(self):
        self.test_user_one = User.objects.create_user('JohnD', 'johnd@mail.com', 'johnpassword')
        self.test_user_two = User.objects.create_user('JoshD', 'joshd@mail.com', 'joshpassword')
    def test_str(self):
        test_user_one = self.test_user_one
        test_user_two = self.test_user_two
        Like.give_like(test_user_one, test_user_two)
        Dislike.give_dislike(test_user_one, test_user_two)
        test_like, created = Like.objects.get_or_create(current_user=test_user_two)
        self.assertEqual(str(test_like), "JoshD is liked by 0 users!")

""" Tests if no more than one like can be made from one user to another """
class OnlyOneLikeTest(TestCase):
    def setUp(self):
        self.test_user_one = User.objects.create_user('JohnD', 'johnd@mail.com', 'johnpassword')
        self.test_user_two = User.objects.create_user('JoshD', 'joshd@mail.com', 'joshpassword')
    def test_str(self):
        test_user_one = self.test_user_one
        test_user_two = self.test_user_two
        Like.give_like(test_user_one, test_user_two)
        Like.give_like(test_user_one, test_user_two)
        Like.give_like(test_user_one, test_user_two)
        Like.give_like(test_user_one, test_user_two)
        Like.give_like(test_user_one, test_user_two)
        test_like, created = Like.objects.get_or_create(current_user=test_user_two)

        self.assertEqual(str(test_like), "JoshD is liked by 1 users!")

""" Tests if no more than one dislike can be made from one user to another """
class OnlyOneDislikeTest(TestCase):
    def setUp(self):
        self.test_user_one = User.objects.create_user('JohnD', 'johnd@mail.com', 'johnpassword')
        self.test_user_two = User.objects.create_user('JoshD', 'joshd@mail.com', 'joshpassword')
    def test_str(self):
        test_user_one = self.test_user_one
        test_user_two = self.test_user_two
        Dislike.give_dislike(test_user_one, test_user_two)
        Dislike.give_dislike(test_user_one, test_user_two)
        Dislike.give_dislike(test_user_one, test_user_two)
        Dislike.give_dislike(test_user_one, test_user_two)
        Dislike.give_dislike(test_user_one, test_user_two)
        test_dislike, created = Dislike.objects.get_or_create(current_user=test_user_two)

        self.assertEqual(str(test_dislike), "JoshD is disliked by 1 users!")
