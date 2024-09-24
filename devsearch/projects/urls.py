from django.urls import path

from . import views

urlpatterns = [
    path("projects/", views.projects_page, name="projects"),
    path("project/<int:pk>/", views.single_project_page, name="project"),
]
