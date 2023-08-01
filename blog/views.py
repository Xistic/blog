from django.shortcuts import render
from django.views.generic.base import View
from .models import Notes
from .models import Resume
from .models import Project
from django.shortcuts import render

class Main(View):
    '''Главная страница'''
    def get(self, request):
        return render(request, 'blog/main.html')

from django.views import View
from django.shortcuts import render
from .models import Notes
from .models import Project
class NoteView(View):
    '''Вывод заметок'''
    def get(self, request):
        notes = list(Notes.objects.all())
        notes.reverse()
        hello_world_note = None
        for note in notes:
            if note.title == "Hello world":
                hello_world_note = note
                notes.remove(note)
                break
        if hello_world_note:
            notes.insert(0, hello_world_note)
        return render(request, 'blog/my_notes.html', {'note_list': notes})

class ResumeView(View):
    '''Вывод страницы резюме'''
    def get(self, request):
        projects = list(Project.objects.all())
        resume = list(Resume.objects.all())
        context = {'resume': resume, 'projects': projects}
        return render(request, 'blog/resume.html', context)

class Roadmap(View):
    '''Вывод страницы карты'''
    def get(self, request):
        return render(request, 'blog/roadmap.html')