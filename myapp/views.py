from django.shortcuts import render
from .models import Person


def index(request):
    return render(request, "index.html", {"persons": Person.objects.all()})
