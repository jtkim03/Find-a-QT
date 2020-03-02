from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    context = {}
    return render(request,'find_a_qt/home.html',context)

def about_view(request):
    return render(request,'find_a_qt/about.html')