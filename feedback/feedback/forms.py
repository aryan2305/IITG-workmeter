from gc import get_objects

from django import forms
from django.core import validators

from organisation.models import Gymkhana_body


def must_be_empty(value):
    if value:
        raise forms.ValidationError('is not empty')


class QuestionForm(forms.Form):
    body = forms.ModelChoiceField(queryset=Gymkhana_body.objects.all())
    question = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'myfieldclass'}))
    choice1 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'myfieldclass'}))
    choice2 = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'myfieldclass'}))
    choice3 = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'myfieldclass'}))
    choice4 = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'myfieldclass'}))

    def clean(self):
        cleaned_data = super().clean()
