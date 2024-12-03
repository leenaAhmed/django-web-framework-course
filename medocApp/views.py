from django.http import HttpResponse
from django.shortcuts import render


def handler404(request , exception):
    return render(request, 'pages/notfound.html')