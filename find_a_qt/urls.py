from django.urls import path

from . import views
from django.contrib.staticfiles.URLs import staticfiles_urlpatterns
from .views import QuestionListView, QuestionDetailView, QuestionCreateView,search_view

urlpatterns = [
    path('', views.home_view, name='index'),
    path('about', views.about_view, name = 'about'),
    path('studentregister', views.student_register, name = 'studentregister'),
    path('tutorregister', views.tutor_register, name = 'tutorregister'),
    path('questions', QuestionListView.as_view(), name = 'viewquestions'),
    path('questions/new/', QuestionCreateView.as_view(), name='createquestions'),
    path('questions/<int:pk>/', QuestionDetailView.as_view(), name = 'viewquestions-detail'),
    path('questions/search/', views.search_view, name = 'search'),
]
