from django.contrib import admin
from .models import ClassLevel, ClassArm, Subject, SubjectOffering, Student

admin.site.register(ClassLevel)
admin.site.register(ClassArm)
admin.site.register(Subject)
admin.site.register(SubjectOffering)
admin.site.register(Student)
