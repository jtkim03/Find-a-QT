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
from find_a_qt.views import home, student_register, tutor_register, QuestionListView, QuestionDetailView, QuestionCreateView
from django.views.generic import TemplateView
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static


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
    path('profile/', user_views.view_profile, name='profile'),
    path('profile/edit/', user_views.edit_profile, name='edit_profile'),

    path('questions/', QuestionListView.as_view(), name='viewquestions'),
    path('questions/new/', QuestionCreateView.as_view(), name='createquestions'),
    path('questions/<int:pk>/', QuestionDetailView.as_view(), name = 'viewquestions-detail'),

    path('reset-password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset-password/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    re_path(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,23})/$',
            auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset-password/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



