from django.shortcuts import render, HttpResponse, redirect
from .models import Todo
from .models import Books
from .models import Price



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
    title = form["books_title"]
    books_title = Books(title=title)
    books_title.save()

    subtitle = form["books_subtitle"] 
    books_subtitle = Books(subtitle=subtitle)
    books_subtitle.save()

    description = form["books_description"]
    books_description = Books(description=description)
    books_description.save()

    genre = form["books_genre"] 
    books_genre = Books(genre=genre)
    books_genre.save()

    author = form["books_author"]
    books_author = Books(author=author)
    books_author.save()

    cost_amount = form["books_price"]
    currency = form["books_price"]
    books_price = Price(cost_amount=cost_amount, currency=currency)
    books_price.save()

    year = form["books_year"]
    books_year = Books(year=year)
    books_year.save()

    date = form["books_date"]
    books_date = Books(date=date)
    books_date.save()
    # todo = Books(title=title, subtitle=subtitle, description=description, genre=genre, author=author, price=price, year=year, date=date)
    books_date.save()
    return redirect(second)
    # return HttpResponse("Form received")



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

