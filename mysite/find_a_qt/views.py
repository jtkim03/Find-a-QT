from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    template = "homepage.html"
    context = {}
    return render(request,template,context)