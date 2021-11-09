from django.shortcuts import render, HttpResponse


def homepage(request):
    return render(request, "index.html")


def test(req):
    return render(req, "test.html")
