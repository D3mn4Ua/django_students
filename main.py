import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from students.models import Teacher, Subject, Class, Student

teacher = Teacher.objects.create(
    name="Teacher1"
)
teacher1 = Teacher.objects.create(
    name="Teacher2"
)
subject = Subject.objects.create(
    title="Physics"
)

subject.teachers.add(teacher, teacher1)

student = Student.objects.create(
    name="Student1"
)
student1 = Student.objects.create(
    name="Student2"
)
classes = Class.objects.create(
    title="Class_number_one"
)

classes.students.add(student, student1)