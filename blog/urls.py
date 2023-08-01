from django.urls import path
from . import views

urlpatterns = [
    path('', views.Main.as_view(), name='main_page'),
    path('notes', views.NoteView.as_view(), name='notes_page'),
    path('resume', views.ResumeView.as_view(), name='resume_page'),
    path('roadmap/', views.Roadmap.as_view(), name='roadmap_page'),
]
