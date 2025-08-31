from django.db import models


class ClassLevel(models.Model):
    name = models.CharField(max_length=20, unique=True)  # e.g., JSS1, SS2

    def __str__(self):
        return self.name


class ClassArm(models.Model):
    class_level = models.ForeignKey(ClassLevel, on_delete=models.CASCADE)
    arm = models.CharField(max_length=2)  # e.g., A, B, C

    class Meta:
        unique_together = ("class_level", "arm")

    def __str__(self):
        return f"{self.class_level.name}-{self.arm}"


class Subject(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class SubjectOffering(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    class_level = models.ForeignKey(ClassLevel, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("subject", "class_level")

    def __str__(self):
        return f"{self.subject.name} ({self.class_level.name})"


class Student(models.Model):
    admission_no = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=[("M", "Male"), ("F", "Female")])
    dob = models.DateField()
    class_arm = models.ForeignKey(ClassArm, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.admission_no})"
