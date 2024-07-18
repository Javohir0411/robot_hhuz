from django.contrib.auth import get_user_model
from django.db import models


class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        db_table = 'abstract_model'


class Vacancy(AbstractBaseModel):
    vacancy_name = models.CharField(max_length=400, blank=True, null=True)
    area_name = models.CharField(max_length=255, blank=True, null=True)
    salary_from = models.IntegerField(blank=True, null=True)
    salary_to = models.IntegerField(blank=True, null=True)
    currency = models.CharField(max_length=3, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=255, default=None, blank=True, null=True)
    building = models.CharField(max_length=100, default=None, blank=True, null=True)
    employer_name = models.CharField(max_length=355, blank=True, null=True)
    requirements = models.TextField(blank=True, null=True)
    responsibilities = models.TextField(blank=True, null=True)
    exp_from = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return f"Вакансия: {self.vacancy_name}, Зарплата:{self.salary_from + self.salary_to // 2}, Опыт {self.exp_from}"

    class Meta:
        verbose_name = "Vacancy"
        verbose_name_plural = "Vacancies"
        db_table = 'vacancies'


