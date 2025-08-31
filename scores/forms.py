from django import forms
from .models import Score


class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ["student", "subject", "score", "term"]
        widgets = {
            "student": forms.Select(attrs={"class": "form-control"}),
            "subject": forms.Select(attrs={"class": "form-control"}),
            "score": forms.NumberInput(attrs={"class": "form-control"}),
            "term": forms.Select(attrs={"class": "form-control"}),
        }

    def clean_score(self):
        score = self.cleaned_data.get("score")
        if score < 0 or score > 100:
            raise forms.ValidationError("Score must be between 0 and 100")
        return score
