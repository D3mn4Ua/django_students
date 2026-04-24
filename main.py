import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from students.models import Teacher, Subject

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