from django import forms
from django.forms import ModelForm
from .models import Vacancy


class VacancyForm(ModelForm):
    class Meta:
        model = Vacancy
        fields = "__all__"


class RpaForm(ModelForm):
    class Meta:
        model = Vacancy
        fields = ('vacancy_name',)


class SearchForm(forms.Form):
    text = forms.CharField(label='Search', max_length=255)
