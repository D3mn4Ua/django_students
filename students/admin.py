from django.contrib import admin
from .models import Teacher, Subject, Student, Class, Grade, Schedule

admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Class)
admin.site.register(Grade)
admin.site.register(Schedule)