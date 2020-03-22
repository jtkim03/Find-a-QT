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
from django.urls import path, include
from find_a_qt.views import home, student_register, tutor_register
from django.views.generic import TemplateView
from users import views as user_views


urlpatterns = [
    path('',TemplateView.as_view(template_name = 'find_a_qt/home.html'), name='faqt-home'), #TODO Merge this login template with homepage
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('about/', TemplateView.as_view(template_name = 'find_a_qt/about.html')),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name = 'logout'),
    path('studentregister/', student_register, name='studentregister'),
    #path('addstudent/', add_student, name='addstudent')
    path('tutorregister/', tutor_register, name='tutorregister'),
    path('profile/', user_views.profile, name='profile'),
]

