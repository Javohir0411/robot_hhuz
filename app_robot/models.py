from django.contrib.auth import get_user_model
from django.db import models


class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        abstract = True
        db_table = 'abstract_model'


class Vacancy(AbstractBaseModel):
    vacancy_name = models.CharField(max_length=400)
    area_name = models.CharField(max_length=255)
    salary_from = models.IntegerField()
    salary_to = models.IntegerField()
    currency = models.CharField(max_length=3)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    building = models.CharField(max_length=100, default=None)
    raw = models.TextField()
    employer_name = models.CharField(max_length=355)
    requirements = models.TextField()
    responsibilities = models.TextField()
    exp_from = models.IntegerField()
    exp_to = models.IntegerField()

    def __str__(self):
        return f"Вакансия: {self.vacancy_name}, Зарплата:{self.salary_from + self.salary_to // 2}, Опыт {self.exp_from}"

    class Meta:
        verbose_name = "Vacancy"
        verbose_name_plural = "Vacancies"
        db_table = 'vacancies'
