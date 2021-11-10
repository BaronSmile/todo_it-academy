from django.shortcuts import render, HttpResponse
from .models import ToDo


def homepage(request):
    return render(request, "index.html")


def test(req):
    return render(req, "test.html", )


def test2(req):
    todo_list = ToDo.objects.all()
    return render(req, "test2.html", {"todo_list": todo_list})
