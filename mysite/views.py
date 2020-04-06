from django.shortcuts import render, redirect
from django.http import HttpResponse
from find_a_qt.forms import StudentRegistration
from django.contrib import messages


# Create your views here.
def about_view(request):
    return render(request,'find_a_qt/about.html')
def home_view(request):
    return render(request,'find_a_qt/home.html')


"""def student_register_view(request):
    return render(request, 'users/studentregister.html')

def tutor_register_view(request):
    return render(request, 'user/tutorregister.html')"""

