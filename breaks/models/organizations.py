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


