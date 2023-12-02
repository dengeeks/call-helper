from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Organization(models.Model):
    """ Организация """
    name = models.CharField(verbose_name='Название', max_length=255)
    director = models.ForeignKey(
        User, on_delete=models.RESTRICT, related_name='organization_directors',
        verbose_name='Директор',
    )
    employees = models.ManyToManyField(
        User, verbose_name='Сотрудники', related_name='organization_employees',
        blank=True,
    )

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
        ordering = ['name']

    def __str__(self):
        return f'{self.name} ({self.pk})'


class Group(models.Model):
    organization = models.ForeignKey(
        'breaks.Organization', models.CASCADE, related_name='groups',
        verbose_name='Организация',
    )
    name = models.CharField('Название', max_length=255)
    manager = models.ForeignKey(
        User, models.RESTRICT, related_name='group_managers',
        verbose_name='Менеджер',
    )
    employees = models.ManyToManyField(
        User, verbose_name='Сотрудники', related_name='group_employees',
        blank=True,
    )
    min_active = models.PositiveSmallIntegerField(
        'Минимальное количество активных сотрудников', null=True, blank=True,
    )
    break_start = models.TimeField('Начало Обеда', null=True, blank=True)
    break_end = models.TimeField('Конец Обеда', null=True, blank=True)
    break_max_duration = models.PositiveSmallIntegerField('Максимальное длительность обеда', null=True, blank=True)

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ['name']

    def __str__(self):
        return f'{self.name} ({self.pk})'
