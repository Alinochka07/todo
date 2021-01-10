from django.shortcuts import render, HttpResponse



def homepage(requests):
    return HttpResponse("hello world")

def test(request):
    return render(request, "test.html")
