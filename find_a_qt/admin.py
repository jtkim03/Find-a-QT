from django.contrib import admin
from .models import Student, Tutor, Question

admin.site.register(Tutor)
admin.site.register(Student)
admin.site.register(Question)

# Register your models here.
