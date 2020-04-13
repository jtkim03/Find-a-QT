from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.forms import ModelForm
from .models import Student, Tutor, Question, Answer
from phonenumber_field.modelfields import PhoneNumberField
from chat.models import Room



class StudentRegistration(forms.ModelForm):

  # user =

    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'year_in_school', 'major', 'phone_number')
        widgets = {
            'first_name' : forms.TextInput(
                attrs={'class' : 'form-control',
                       'placeholder' : 'Enter First Name',
                       'aria-label' : 'Student',
                       'aria-describedby' : 'add-btn',
                       'size': 1}
            ),
            'last_name' : forms.TextInput(
                attrs={'class' : 'form-control',
                       'placeholder' : 'Enter Last Name',
                       'aria-label' : 'Student',
                       'aria-describedby' : 'add-btn',
                       'size': 1}
            ),
            '''
            'major': forms.TextInput(
                attrs={'class' : 'form-control',
                       'placeholder' : 'Enter Major',
                       'aria-label' : 'Student',
                       'aria-describedby' : 'add-btn'}
            ),
            '''
            'phone_number': forms.TextInput(
             attrs={'class' : 'form-control',
                   'placeholder' : 'Enter Phone Number',
                   'aria-label' : 'Student',
                   'aria-describedby' : 'add-btn'}
        )
    }



class TutorRegistrationForm(forms.ModelForm):

    class Meta:
        model = Tutor
        fields = ('first_name', 'last_name', 'year_in_school', 'major', 'phone_number') #Add bio later
        widgets = {
            'first_name' : forms.TextInput(
                attrs={'class' : 'form-control',
                       'placeholder' : 'Enter First Name',
                       'aria-label' : 'Student',
                       'aria-describedby' : 'add-btn',
                       'size': 1}
            ),
            'last_name' : forms.TextInput(
                attrs={'class' : 'form-control',
                       'placeholder' : 'Enter Last Name',
                       'aria-label' : 'Student',
                       'aria-describedby' : 'add-btn',
                       'size': 1}
            ),
            '''
            'major': forms.TextInput(
                attrs={'class' : 'form-control',
                       'placeholder' : 'Enter Major',
                       'aria-label' : 'Student',
                       'aria-describedby' : 'add-btn'}
            ),
            '''
            'phone_number': forms.TextInput(
                attrs={'class' : 'form-control',
                       'placeholder' : 'Enter Phone Number',
                       'aria-label' : 'Student',
                       'aria-describedby' : 'add-btn'}
            ),
            # 'bio': forms.TextInput(
            #     attrs={'class' : 'form-control',
            #            'placeholder' : 'Enter Phone Number',
            #            'aria-label' : 'Student',
            #            'aria-describedby' : 'add-btn'}
            # )
        }

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('body', 'topic', 'class_name', 'urgency', 'session_date', 'session_time', 'image',)

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('post', 'text', 'upvotes')

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('name', 'description', 'slug')

#class