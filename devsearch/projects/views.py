from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def projects_page(request: HttpRequest) -> HttpResponse:
    return render(request, "projects/index.html")


def single_project_page(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, "projects/single.html")
