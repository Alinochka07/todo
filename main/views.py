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
    form = request.POST
    text = form["book_title", "book_subtitle", "book_description", "book_genre", "book_author"]
    number = form["book_price"]
    date = form["book_year"]
    todo = Books(text=text, number=number, date=date)
    todo.save()
    return redirect(books)
    # return HttpResponse("This is new test 2 page!")
    # return render(request, "books.html", {"books_list": books_list})

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = Todo(text=text)
    todo.save()
    return redirect(test)



# def books(request):
#     return render(request, "books.html")