from django.shortcuts import render
# Create your views here.


def homepage(request):
    return render(request, 'main/index.html',)


def test(request):
    return render(request, 'main/test.html')
