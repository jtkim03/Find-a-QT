"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include, re_path
from find_a_qt.views import home, QuestionListView, \
    QuestionDetailView, question_post, answer_post, room_post, \
    AnswerListView, user_history, UserQuestionView, question_answers, upvote_question_detail,\
    upvote_answer_question, downvote_question_detail, downvote_answer_question
from django.views.generic import TemplateView
from users import views as user_views
from find_a_qt import views as find_a_qt_views
from django.conf import settings
from django.conf.urls.static import static

from chat.models import Room
from find_a_qt.models import Question

urlpatterns = [
    path('',TemplateView.as_view(template_name = 'find_a_qt/home.html'), name='faqt-home'), #TODO Merge this login template with homepage
    path('admin/', admin.site.urls),
    url(r'^', include('chat.urls')),
    path('accounts/', include('allauth.urls')),
    path('about/', TemplateView.as_view(template_name = 'find_a_qt/about.html')),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name = 'logout'),
    path('profile/', user_views.view_profile, name='profile'),
    url(r'^profile/(?P<pk>\d+)/$', user_views.view_profile, name='profile_with_pk'),
    path('profile/edit/', user_views.edit_profile, name='edit_profile'),
    #path('profile/MyQuestions/', UserQuestionView.as_view(), name='myqs'),

    url(r'^profile/(?P<username>\w+)/$', user_views.profile_page, name='public_profile'),

    path('questions/', QuestionListView.as_view(), name='viewquestions'),
    path('answers/', AnswerListView.as_view(), name='viewanswers'),
    path('questions/new/', question_post, name='createquestions'),
    path('questions/<int:pk>/', QuestionDetailView.as_view(), name = 'viewquestions-detail'),
    path('choose_question', TemplateView.as_view(template_name = 'find_a_qt/choose_question.html')),
    path('questions/search/', TemplateView.as_view(template_name = 'find_a_qt/search_question.html'), name = 'search'),
    path('s/', find_a_qt_views.search_view, name = 'search'),
    path('answer/new/', answer_post, name='createqs'),
    path('chat/new/', room_post, name='createroom'),

    path('reset-password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset-password/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    re_path(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,23})/$',
            auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset-password/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('my-questions/', user_history, name='user_question'),
    # path('answer-question/',question_answers,name='answer_question'),
    path('answers/<int:pk>/',question_answers,name='answer_question'),
    url(r'^like/(?P<username>\w+)/$', user_views.like, name='like'),
    url(r'^dislike/(?P<username>\w+)/$', user_views.dislike, name='dislike'),
    url(r'^upvote_q_d/(?P<answer_id>\d+)/(?P<pk>\d+)/$', upvote_question_detail, name='upvote_question_detail'),
    url(r'^upvote_a_q/(?P<answer_id>\d+)/(?P<pk>\d+)/$', upvote_answer_question, name='upvote_answer_question'),
    url(r'^downvote_q_d/(?P<answer_id>\d+)/(?P<pk>\d+)/$', downvote_question_detail, name='downvote_question_detail'),
    url(r'^downvote_a_q/(?P<answer_id>\d+)/(?P<pk>\d+)/$', downvote_answer_question, name='downvote_answer_question'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



