from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.


def index(request):
    data = {'name':"marina", 
            'url':'http://facebook.com',
            'age': '' , 
            'full_name': 'Lina ahmed elhosary',
            "fileSize": 4444444444444
            }
    return render(request,'pages/index.html', data)

def about(request):
    return render(request,'pages/about.html')
