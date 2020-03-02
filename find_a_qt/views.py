from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import StudentRegistration, TutorRegistrationForm
from django import forms
from .models import Student

# Create your views here.
def about_view(request):
    return render(request,'find_a_qt/about.html')
def home(request):
    context = {}
    return render(request,'find_a_qt/home.html',context)


def student_register(request):
    context = {}
    form = StudentRegistration(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        context['form'] = form
        return render(request, 'find_a_qt/home.html', context)

    context['form'] = form
    return render(request, 'users/studentregister.html', context)

def tutor_register(request):
    context = {}
    form = TutorRegistrationForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        context['form'] = form
        return render(request, 'find_a_qt/home.html', context)


    context['form'] = form

    return render(request, 'users/tutorregister.html', context)
