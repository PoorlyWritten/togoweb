from django import forms
from .models import QuizzProfile

class ReportForm(forms.Form):
    report = forms.CharField()

class SupporterForm(forms.ModelForm):
    class Meta:
        model = QuizzProfile
        fields = ('quiz_relationship', 'quiz_event', 'email')

