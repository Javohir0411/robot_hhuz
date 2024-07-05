from django.shortcuts import render, redirect
from .forms import VacancyForm, RpaForm
from .models import Vacancy


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
    vacancy = Vacancy.objects.all()
    return render(request, 'vacancies.html', {'vacancy': vacancy})


# def rpa(request):
#     vacancy = Vacancy.objects.all()
#     return render(request, 'rpa.html', {'vacancy': vacancy})

def rpa_view(request):
    if request.method == 'POST':
        form = RpaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = RpaForm()
    return render(request, 'rpa.html', {'form': form})
