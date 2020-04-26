from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.forms import ModelForm
from .models import Student, Tutor, Question, Answer
from phonenumber_field.modelfields import PhoneNumberField
from chat.models import Room


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('body', 'topic', 'class_name', 'urgency', 'image')

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('post', 'text', 'upvotes', 'image')

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('name', 'description', 'slug')

#class