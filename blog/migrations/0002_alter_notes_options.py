# Generated by Django 4.2.2 on 2023-06-29 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notes',
            options={'verbose_name': 'Заметка', 'verbose_name_plural': 'Заметки'},
        ),
    ]
