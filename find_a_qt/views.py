from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from .forms import QuestionForm, AnswerForm, RoomForm
from django import forms
from .models import Student, Question, Answer
from allauth.socialaccount.models import SocialAccount
from django.template import RequestContext
import operator

from chat.models import Room

from django.db.models import Q

from django.views.generic import ListView, DetailView, CreateView

# Create your views here.
def about_view(request):
    return render(request,'find_a_qt/about.html')
def home(request):
    context = {}
    return render(request,'find_a_qt/home.html',context)

def search_view(request):
    try:
        k = request.GET.get('k')
    except:
        k = None
    if k:
        questions = Question.objects.filter(class_name__icontains= k)
        context = {'query': k, 'questions':questions}
        template = 'find_a_qt/search_results.html'
    else:
        template = 'find_a_qt/search_question.html'
    return render(request,template,context)


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

class UserQuestionView(ListView):
    model = Question
    template_name = 'user_posts.html'

    def get_query_set(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Question.objects.filter(author=user)


def answer_post(request):
    context = {}
    form = AnswerForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.author_name = request.user.username
        context['form'] = form
        text = form.cleaned_data.get('text')
        upvotes = form.cleaned_data.get('upvotes')
        instance.save()
        messages.success(request, f'Success! Answer posted.')
        return HttpResponseRedirect('/questions/')

    context['form'] = form
    return render(request, 'find_a_qt/answer_form.html', context)

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
        image = form.cleaned_data.get('image')
        instance.save()
        messages.success(request, f'Success! Created question {body}!')
        #return render(request, 'find_a_qt/question_form.html', context)
        return HttpResponseRedirect('/questions/')

    context['form'] = form
    return render(request, 'find_a_qt/question_form.html', context)

def user_history(request):
    history = Question.objects.filter(author_name=request.user).values()
    return render(request,'find_a_qt/user_questions.html',{'history':history})

def question_answers(request,pk):

    questions = Question.objects.filter(id=pk).values()
    history = Answer.objects.filter(post_id=pk).values()
    get_question = Question.objects.get(pk=pk)
    return render(request,'find_a_qt/answer_question.html',{'history': history, 'questions': questions,
                                                            'get_question':get_question})


@login_required
def upvote_question_detail(request,answer_id,pk):

    answer = Answer.objects.get(id=answer_id)
    answer.upvotes.add(request.user)
    answer.downvotes.remove(request.user)
    #answer.save()
    return redirect('/questions/' + str(pk))

@login_required
def upvote_answer_question(request,answer_id,pk):

    answer = Answer.objects.get(id=answer_id)
    answer.upvotes.add(request.user)
    answer.downvotes.remove(request.user)
    #answer.save()
    return redirect('/answers/' + str(pk))

@login_required
def downvote_question_detail(request,answer_id,pk):
    answer = Answer.objects.get(id=answer_id)
    answer.downvotes.add(request.user)
    answer.upvotes.remove(request.user)
    #answer.save()
    return redirect('/questions/' + str(pk))

@login_required
def downvote_answer_question(request,answer_id,pk):
    answer = Answer.objects.get(id=answer_id)
    answer.downvotes.add(request.user)
    answer.upvotes.remove(request.user)
    #answer.save()
    return redirect('/answers/' + str(pk))
