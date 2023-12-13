# Generated by Django 4.2.7 on 2023-12-04 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('breaks', '0010_break_duration'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='break',
            options={'ordering': ['-replacement__date', 'break_start'], 'verbose_name': 'Обеденный перерыв', 'verbose_name_plural': 'Обеденные перерывы'},
        ),
        migrations.RemoveField(
            model_name='break',
            name='duration',
        ),
    ]
