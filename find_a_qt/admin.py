from django.contrib import admin
from .models import Student, Tutor, Question, Answer

admin.site.register(Tutor)
admin.site.register(Student)
admin.site.register(Question)
admin.site.register(Answer)

# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['body', 'topic', 'class_name', 'author_name', 'urgency', 'session_date', 'image']

#     def save_model(self, request, obj, form, change):
#         if getattr(obj, 'author_name', None) is None:
#             obj.author_name = request.user.username
#         obj.save()
# Register your models here.
