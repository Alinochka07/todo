from django.shortcuts import render, HttpResponse



def homepage(request):
    return render(request, "index.html")

def test(request):
    return render(request, "test.html")

def second(request):
    return HttpResponse("This is new test 2 page!")

def third(request):
    return HttpResponse("This is page test 3")

def task31(request):
    return HttpResponse("Ваша запись была добавлена успешно.")

def task31_2(request):
    return HttpResponse("Ваша запись была изменена успешно.")

def task31_3(request):
    return HttpResponse("Ваша запись была удалена.")
