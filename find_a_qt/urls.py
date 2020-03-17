from django.urls import path

from . import views
from django.contrib.staticfiles.URLs import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home_view, name='index'),
    path('about', views.about_view, name = 'about'),
    path('studentregister', views.student_register, name = 'studentregister'),
    path('tutorregister', views.tutor_register, name = 'tutorregister'),
]
