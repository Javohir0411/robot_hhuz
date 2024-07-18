from django.shortcuts import redirect
from django.shortcuts import render
from .forms import VacancyForm
from .forms import SearchForm
from .models import Vacancy
import requests


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

# def rpa_view(request):
#     if request.method == 'POST':
#         form = RpaForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('main')
#     else:
#         form = RpaForm()
#     return render(request, 'rpa.html', {'form': form})


def scrape_vacancies(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search_text = form.cleaned_data['text']
            uzb_id = None
            url = 'https://api.hh.ru/vacancies'
            areas_url = 'https://api.hh.ru/areas'
            areas_response = requests.get(areas_url)
            areas_data = areas_response.json()
            for area in areas_data:
                if area['name'].lower() == 'узбекистан':
                    uzb_id = area['id']
            params = {
                'text': search_text,
                'area': uzb_id,
                'page': 0,
                'per_page': 20
            }
            response = requests.get(url, params=params)
            data = response.json()
            vacancies = data['items']
            for vacancy in vacancies:
                vacancy_name = vacancy['name']
                area_name = vacancy['area']['name']
                salary_from = vacancy['salary']['from'] if vacancy['salary'] else None
                salary_to = vacancy['salary']['to'] if vacancy['salary'] else None
                currency = vacancy['salary']['currency'] if vacancy['salary'] else None
                city = vacancy['address']['city'] if vacancy['address'] else None
                street = vacancy['address']['street'] if vacancy['address'] else None
                building = vacancy['address']['building'] if vacancy['address'] else None
                employer_name = vacancy['employer']['name']
                requirements = vacancy['snippet']['requirement']
                responsibilities = vacancy['snippet']['responsibility']
                exp_from = vacancy['experience']['name']

                Vacancy.objects.create(
                    vacancy_name=vacancy_name,
                    area_name=area_name,
                    salary_from=salary_from,
                    salary_to=salary_to,
                    currency=currency,
                    city=city,
                    street=street,
                    building=building,
                    employer_name=employer_name,
                    requirements=requirements,
                    responsibilities=responsibilities,
                    exp_from=exp_from,
                )
            return render(request, 'scrape_vacancies.html', {'form': form, 'vacancies': Vacancy.objects.all()})
    else:
        form = SearchForm()
    return render(request, 'scrape_vacancies.html', {'form': form, 'vacancies': Vacancy.objects.all()})


"""
 Vacancy.objects.create(
                    vacancy_name=vacancy_name,
                    area_name=area_name,
                    salary_from=salary_from,
                    salary_to=salary_to,
                    currency=currency,
                    city=city,
                    street=street,
                    building=building,
                    employer_name=employer_name,
                    requirements=requirements,
                    responsibilities=responsibilities,
                    exp_from=exp_from,
                )
"""
