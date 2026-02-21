from django.urls import path
from . import views

urlpatterns = [
  path('notes/', views.NoteDelete.as_view(), name="note-lisy"),
  path('notes/delete/<int:pk>/', views.NoteDelete.as_view(), name="delete-note")
] 