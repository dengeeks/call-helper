from django.contrib.auth import get_user_model
from django.db import models
from common.models.mixins import BaseDictModelMixin

User = get_user_model()


class ReplacementStatus(BaseDictModelMixin):
    class Meta:
        verbose_name = 'Статус смены'
        verbose_name_plural = 'Статусы смены'
        ordering = ('sort',)


class Replacement(models.Model):
    group = models.ForeignKey('breaks.Group', models.CASCADE, 'replacements',
                              verbose_name='Группа'
                              )
    date = models.DateField('Дата смены')
    breaks_start = models.TimeField('Начало обеда')
    breaks_end = models.TimeField('Конец обеда')
    breaks_max_duration = models.IntegerField(
        'Макс. продолжительность обеда'
    )

    class Meta:
        verbose_name = 'Смена'
        verbose_name_plural = 'Смены'
        ordering = ('-date',)

    def __str__(self):
        return f'Смена №{self.pk} для {self.group}'


class ReplacementEmployee(models.Model):
    employee = models.ForeignKey(User, models.CASCADE, 'replacements',
                                 verbose_name='Группа')
    replacement = models.ForeignKey(
        'breaks.Replacement', models.CASCADE, 'employees',
        verbose_name='Смена'
    )
    status = models.ForeignKey(
        'breaks.ReplacementStatus', models.RESTRICT, 'replacement_employees',
        verbose_name='Статус'
    )

    class Meta:
        verbose_name = 'Смена - Работник'
        verbose_name_plural = 'Смены - Работники'

    def __str__(self):
        return f'Смена {self.replacement} для {self.employee}'
