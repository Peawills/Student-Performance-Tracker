from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["first_name", "last_name", "student_class", "age"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "student_class": forms.Select(attrs={"class": "form-control"}),
            "age": forms.NumberInput(attrs={"class": "form-control"}),
        }
        