from django.contrib import admin
from .models import Vacancy


class VacancyAdmin(admin.ModelAdmin):
    list_display = ('id', 'vacancy_name', 'salary_to')
    search_fields = ('vacancy_name',)
    ordering = ['id']


admin.site.register(Vacancy, VacancyAdmin)
