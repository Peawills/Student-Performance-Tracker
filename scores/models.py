from django.db import models
from students.models import Student, Subject


class Session(models.Model):
    name = models.CharField(max_length=20, unique=True)  # e.g., 2024/2025
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Score(models.Model):
    TERM_CHOICES = [
        ("FIRST", "First Term"),
        ("SECOND", "Second Term"),
        ("THIRD", "Third Term"),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    term = models.CharField(max_length=10, choices=TERM_CHOICES)
    score = models.PositiveIntegerField()
    date_recorded = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("student", "subject", "session", "term")

    def __str__(self):
        return f"{self.student} - {self.subject} ({self.term} {self.session})"
