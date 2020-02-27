from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    context = {}
    return render(request,'find_a_qt/home.html',context)

def detail(request, tutor_id):
    return HttpResponse("You're looking at question %s." % tutor_id)