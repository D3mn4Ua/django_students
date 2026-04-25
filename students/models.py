from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=63)

class Subject(models.Model):
    title = models.CharField(max_length=63)
    teachers = models.ManyToManyField(Teacher, related_name="subjects")

###

class Student(models.Model):
    name = models.CharField(max_length=63)

class Class(models.Model):
    title = models.CharField(max_length=63)
    students = models.ManyToManyField(Student, related_name="classes")

###

class Grade(models.Model):
    grade = models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    

class Schedule(models.Model):
    order = models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    classes = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.order}, {self.subject}, {self.classes}" 


