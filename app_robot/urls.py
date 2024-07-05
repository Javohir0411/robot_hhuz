from django.urls import path
from .views import (
    main,
    add_vacancy,
    vacancies,
    rpa_view,
)
urlpatterns = [
    path('', main, name='main'),
    path('add_vacancy/', add_vacancy, name='add_vacancy'),
    path('vacancies/', vacancies, name='vacancies'),
    path('rpa/', rpa_view, name='rpa'),
]
