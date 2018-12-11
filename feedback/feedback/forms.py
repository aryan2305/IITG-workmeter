from gc import get_objects

from django import forms
from django.core import validators

from organisation.models import Gymkhana_body


def must_be_empty(value):
    if value:
        raise forms.ValidationError('is not empty')


class QuestionForm(forms.Form):
    body = forms.ModelChoiceField(queryset=Gymkhana_body.objects.all())
    question = forms.CharField(widget=forms.Textarea)
    choice1 = forms.CharField()
    choice2 = forms.CharField(required=False)
    choice3 = forms.CharField(required=False)
    choice4 = forms.CharField(required=False)

    def clean(self):
        cleaned_data = super().clean()
