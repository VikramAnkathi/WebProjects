from django.shortcuts import render
# Create your views here.


def hi(request):
    return render(request, 'webapp1/webapp1.html')
