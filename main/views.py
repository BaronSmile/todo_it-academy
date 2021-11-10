from django.shortcuts import render, HttpResponse
from .models import ToDo, ToMeet


def homepage(request):
    return render(request, "index.html")


def test(req):
    return render(req, "test.html", )


def test2(req):
    todo_list = ToDo.objects.all()
    return render(req, "test2.html", {"todo_list": todo_list})


def toMeet(req):
    toMeet_list = ToMeet.objects.all()
    return render(req, 'meeting.html', {'toMeet_list': toMeet_list})
