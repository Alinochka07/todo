from django.shortcuts import render, HttpResponse



def homepage(requests):
    return HttpResponse("hello world!")

def test(request):
    return render(request, "test.html")

def second(request):
    return HttpResponse("This is new test 2 page!")

def third(request):
    return HttpResponse("This is page test 3")