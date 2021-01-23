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
    return render(request, "books.html", {"books_list": books_list})

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = Todo(text=text)
    todo.save()
    return redirect(test)


# TASK 
def books_new(request):
    form = request.POST
    book = Book(
        title = form["books_title"],
        subtitle = form["books_subtitle"],
        description = form["books_description"],
        genre = form["books_genre"],
        author = form["books_author"],
        price = form["books_price"],
        year = form["books_year"],
        date = form["books_date"]
    )
    
    book.save()
    return redirect(second)




# todo project
def delete_todo(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect(test)

def mark_todo(request, id):
    todo = Todo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test)
    
def unmark_todo(request, id):
    todo = Todo.objects.get(id=id)
    todo.is_favorite = False
    todo.save()
    return redirect(test)

def close_todo(request, id):
    todo = Todo.objects.get(id=id)
    todo.is_closed = not todo.is_closed
    todo.save()
    return redirect(test)

# TASK MARK

def trash_books(request, id):
    books = Books.objects.get(id=id)
    books.delete()
    return redirect(second)

def mark_books(request, id):
    books = Books.objects.get(id=id)
    books.is_favorites = True
    books.save()
    return redirect(second)
    
def unmark_books(request, id):
    books = Todo.objects.get(id=id)
    books.is_favorites = False
    books.save()
    return redirect(second)