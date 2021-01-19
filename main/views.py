from django.shortcuts import render, HttpResponse
from .models import Todo



def homepage(request):
    return render(request, "index.html")

def test(request):
    todo_list = Todo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def second(request):
    return HttpResponse("This is new test 2 page!")