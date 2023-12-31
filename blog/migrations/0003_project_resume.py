# Generated by Django 4.2.2 on 2023-07-01 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_notes_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=128, verbose_name='Название проекта')),
                ('description', models.TextField(verbose_name='Описание проекта')),
                ('link_project', models.CharField(max_length=512, verbose_name='Ссылка на проект')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=32, verbose_name='Фамилия')),
                ('number', models.CharField(max_length=14, verbose_name='Номер телефона')),
                ('country', models.CharField(max_length=64, verbose_name='Страна проживания')),
                ('city', models.CharField(max_length=32, verbose_name='Город')),
                ('skills', models.TextField(verbose_name='Навыки')),
                ('work_experience', models.TextField(verbose_name='Опыт работы')),
                ('education', models.TextField(verbose_name='Образование')),
            ],
            options={
                'verbose_name': 'Резюме',
                'verbose_name_plural': 'Резюме',
            },
        ),
    ]
