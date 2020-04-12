from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import StudentRegistration, TutorRegistrationForm, QuestionForm, AnswerForm, RoomForm
from django import forms
from .models import Student, Question, Answer
from allauth.socialaccount.models import SocialAccount

from chat.models import Room

from django.db.models import Q

from django.views.generic import ListView, DetailView, CreateView

# Create your views here.
def about_view(request):
    return render(request,'find_a_qt/about.html')
def home(request):
    context = {}
    return render(request,'find_a_qt/home.html',context)

class QuestionListView(ListView):
    model = Question
    template_name = 'find_a_qt/questions.html'
    context_object_name = 'questions'

class AnswerListView(ListView):
    model = Answer
    template_name = 'find_a_qt/answers.html'
    context_object_name = 'answers'

class QuestionDetailView(DetailView):
    model = Question

# class QuestionCreateView(CreateView):
#     model = Question
#     fields = ['body', 'topic', 'class_name', 'author_name', 'urgency', 'session_date', 'image']

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

def answer_post(request):
    context = {}
    form = AnswerForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        context['form'] = form
        text = form.cleaned_data.get('text')
        upvotes = form.cleaned_data.get('upvotes')
        instance.save()
        messages.success(request, f'Success! Created answer!')
        return HttpResponseRedirect('/questions/')

    context['form'] = form
    return render(request, 'find_a_qt/question_form.html', context)

def room_post(request):
    context = {}
    form = RoomForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        context['form'] = form
        #fields = ('name', 'description', 'slug')
        #name = form.cleaned_data.get('name')
        #dscription = form.cleaned_data.get('dscription')
        messages.success(request, f'Success! Created Chat Room!')
        return HttpResponseRedirect('/chat/')

    context['form'] = form
    return render(request, 'find_a_qt/room_form.html', context)


 
def question_post(request):
    context = {}
    form = QuestionForm(request.POST or None, request.FILES or None)


    if form.is_valid():
        instance = form.save(commit=False)
        instance.author_name = request.user.username
        context['form'] = form
        topic = form.cleaned_data.get('topic')
        body = form.cleaned_data.get('body')
        class_name = form.cleaned_data.get('class_name')
        author_name = form.cleaned_data.get('author_name')
        urgency = form.cleaned_data.get('urgency')
        session_date = form.cleaned_data.get('session_date')
        image = form.cleaned_data.get('image')
        instance.save()
        messages.success(request, f'Success! Created question {body}!')
        #return render(request, 'find_a_qt/question_form.html', context)
        return HttpResponseRedirect('/questions/')

    context['form'] = form
    return render(request, 'find_a_qt/question_form.html', context)


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


