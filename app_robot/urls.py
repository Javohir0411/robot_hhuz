from django.urls import path
from .views import (
    main,
    add_vacancy,
    vacancies
)
urlpatterns = [
    path('', main, name='main'),
    path('add_vacancy/', add_vacancy, name='add_vacancy'),
    path('vacancies/', vacancies, name='vacancies'),
]
