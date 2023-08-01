from django.contrib import admin
from .models import Notes, Resume, Project

@admin.register(Notes)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['first_name']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_name']