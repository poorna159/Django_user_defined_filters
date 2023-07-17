from django.shortcuts import render

# Create your views here.


def usdf(request):
    d={'data':'YOU DO NOT FIND THE HAPPY LIFE'}
    return render(request, 'usdf.html',d)

