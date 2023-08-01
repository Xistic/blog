from django.db import models

class Notes(models.Model):
    '''Данные о заметках'''
    title = models.CharField('Заголовок заметки', max_length=100)
    description = models.TextField('Текст заметки')
    date = models.DateField('Дата публикации')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'


class Resume(models.Model):
    '''Резюме'''
    first_name = models.CharField('Имя', max_length=32)
    last_name = models.CharField('Фамилия', max_length=32)
    age = models.IntegerField('Возраст')
    number = models.CharField('Номер телефона', max_length=14)
    email = models.EmailField('Почта', max_length=128)
    country = models.CharField('Страна проживания', max_length=64)
    city = models.CharField('Город', max_length=32)
    skills = models.TextField('Навыки')
    work_experience = models.TextField('Опыт работы')
    education = models.TextField('Образование')

    def __str__(self):
        return f'{self.first_name}'

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'

class Project(models.Model):
    '''Проекты'''
    project_name = models.CharField('Название проекта', max_length=128)
    description = models.TextField('Описание проекта')
    link_project = models.CharField('Ссылка на проект', max_length=512)

    def __str__(self):
        return f'{self.project_name}'

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

