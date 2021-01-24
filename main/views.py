from django.shortcuts import render, HttpResponse, redirect
from .models import Todo
from .models import BookShop

###### Todo project #######

def homepage(request):
    return render(request, "index.html")

def test(request):
    todo_list = Todo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = Todo(text=text)
    todo.save()
    return redirect(test)


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





#### TASK - BOOKS ####

def bookshop(request):
    bookshop_list = BookShop.objects.all()
    return render(request, "books.html", {"bookshop_list": bookshop_list})


def add_book(request):
    form = request.POST
    book = BookShop(
        title = form["books_title"],
        subtitle = form["books_subtitle"],
        description = form["books_description"],
        genre = form["books_genre"],
        author = form["books_author"],
        price = form["books_price"],
        year = form["books_year"],
        books_date = form["books_date"],
        is_favorites = True
    )
    
    book.save()
    return redirect(bookshop)


def trash_books(request, id):
    book = BookShop.objects.get(id=id)
    book.delete()
    return redirect(bookshop)

def mark_books(request, id):
    book = BookShop.objects.get(id=id)
    book.is_favorites = True
    book.save()
    return redirect(bookshop)
    
def unmark_books(request, id):
    book = BookShop.objects.get(id=id)
    book.is_favorites = False
    book.save()
    return redirect(bookshop)