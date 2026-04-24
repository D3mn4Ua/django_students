from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=63)

class Subject(models.Model):
    title = models.CharField(max_length=63)
    teachers = models.ManyToManyField(Teacher, related_name="subjects")