from django.forms import ModelForm
from .models import Vacancy


class VacancyForm(ModelForm):
    class Meta:
        model = Vacancy
        fields = "__all__"


class RpaForm(ModelForm):
    class Meta:
        model = Vacancy
        fields = ("vacancy_name", )
