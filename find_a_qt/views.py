from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import StudentRegistration, TutorRegistrationForm
from django import forms
from .models import Student, Question
from allauth.socialaccount.models import SocialAccount

from django.views.generic import ListView

# Create your views here.
def about_view(request):
    return render(request,'find_a_qt/about.html')
def home(request):
    context = {}
    return render(request,'find_a_qt/home.html',context)

def Q_view(request):
    context = {
        'questions': Question.objects.all()
    }
    return render(request,'find_a_qt/questions.html', context)

class QuestionListView(ListView):
    model = Question
    template_name = 'find_a_qt/questions.html' 
    context_object_name = 'questions'



def student_register(request):
    context = {}
    form = StudentRegistration(request.POST or None, request.FILES or None)


    if form.is_valid():
        form.save()
        context['form'] = form
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        messages.success(request, f'Success! an account has been created for {first_name} {last_name}!')
        return render(request, 'find_a_qt/home.html', context)

    context['form'] = form
    return render(request, 'users/studentregister.html', context)

def tutor_register(request):
    context = {}
    form = TutorRegistrationForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        context['form'] = form
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        messages.success(request, f'Success! an account has been created for {first_name} {last_name}!')
        return render(request, 'find_a_qt/home.html', context)


    context['form'] = form

    return render(request, 'users/tutorregister.html', context)
