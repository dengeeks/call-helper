# Generated by Django 4.2.7 on 2023-12-02 15:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='organization_directors', to=settings.AUTH_USER_MODEL, verbose_name='Директор')),
                ('employees', models.ManyToManyField(null=True, related_name='Сотрудники', to=settings.AUTH_USER_MODEL, verbose_name='organization_employees')),
            ],
            options={
                'verbose_name': 'Организация',
                'verbose_name_plural': 'Организации',
                'ordering': ['name'],
            },
        ),
    ]
