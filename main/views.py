from django.shortcuts import render, HttpResponse, redirect
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

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = Todo(text=text)
    todo.save()
    return redirect(test)


# TASK 33
def books_new(request):
    form = request.POST
    number = form["books_price"]
    todo = Books(number=number)
    todo.save()
    return redirect(books)
    # return HttpResponse("Form received")
    