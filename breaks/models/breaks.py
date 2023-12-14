from django.contrib.auth import get_user_model
from django.db import models
from common.models.mixins import BaseDictModelMixin

User = get_user_model()


class BreakStatus(BaseDictModelMixin):
    class Meta:
        verbose_name = 'Статус обеда'
        verbose_name_plural = 'Статусы обеда'
        ordering = ('sort',)


class Break(models.Model):
    replacement = models.ForeignKey(
        'breaks.Replacement', models.CASCADE, related_name='breaks',
        verbose_name='Смена',
    )
    employee = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Сотрудник', related_name='breaks',
        blank=True,
    )
    break_start = models.TimeField('Начало Обеда', null=True, blank=True)
    break_end = models.TimeField('Конец Обеда', null=True, blank=True)
    status = models.ForeignKey('breaks.BreakStatus', models.RESTRICT, 'breaks', verbose_name="Статус",
                               blank=True)

    class Meta:
        verbose_name = 'Обеденный перерыв'
        verbose_name_plural = 'Обеденные перерывы'
        ordering = ['-replacement__date', 'break_start']

    def __str__(self):
        return f'Обед пользователя {self.employee} ({self.pk})'

    def save(self, *args, **kwargs):
        if not self.pk:
            self.status = BreakStatus.objects.filter(code='created').first()
        return super(Break, self).save(*args, **kwargs)

