# Generated by Django 4.2.7 on 2023-12-03 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breaks', '0005_replacement'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReplacementStatus',
            fields=[
                ('code', models.CharField(max_length=16, primary_key=True, serialize=False, verbose_name='Код')),
                ('name', models.CharField(max_length=32, verbose_name='Название')),
                ('sort', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Сортировка')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активность')),
            ],
            options={
                'verbose_name': 'Статус смены',
                'verbose_name_plural': 'Статус смены',
                'ordering': ('sort',),
            },
        ),
    ]