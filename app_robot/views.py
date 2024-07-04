from django.shortcuts import render, redirect
from django.views.generic import CreateView

from .models import Vacancy
from .forms import VacancyForm


def main(request):
    return render(request, 'main.html')


def add_vacancy(request):
    if request.method == 'POST':
        form = VacancyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = VacancyForm()
        return render(request, 'add_vacancy.html', {'form': form})


def vacancies(request):
    if request.method == 'POST':
        form = VacancyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = VacancyForm()
        return render(request, 'vacancies.html', {'form': form})
