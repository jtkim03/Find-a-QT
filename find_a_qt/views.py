from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    return render(request,'find_a_qt/home.html')

def about_view(request):
    return render(request,'find_a_qt/about.html')