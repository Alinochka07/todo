from django.shortcuts import render, HttpResponse
from .models import Todo
from .models import Books



def homepage(request):
    return render(request, "index.html")

def test(request):
    todo_list = Todo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def second(request):
    books_list = Books.objects.all()
    # return HttpResponse("This is new test 2 page!")
    return render(request, "books.html", {"books_list": books_list})

# def books(request):
#     return render(request, "books.html")