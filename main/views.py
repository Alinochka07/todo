from django.shortcuts import render, HttpResponse
from .models import Todo



def homepage(request):
    return render(request, "index.html")

def test(request):
    return render(request, "test.html")

def second(request):
    return HttpResponse("This is new test 2 page!")