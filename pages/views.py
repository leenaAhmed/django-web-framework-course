from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def about(request):

    path = request.path 
    method = request.method 
    content=f""" 
                <div>
                <h2>Testing Django Request Response Objects</h2> 
                <p>Request path : " {path}</p> 
                <p>Request Method :{method}</p>
                </div> 
            """
    
    # return HttpResponse(content) 
    data = {
        "path": path,
        "method" : method,
    }
    return render(request, 'pages/about.html', {"data": data})


def contactform(request):
    return render(request, 'pages/contact.html')
 

def myview(request):  

      if request.method=='GET':  
        val = request.GET['key'] 
            #perform read or delete operation on the model  

      if request.method=='POST':  
        #perform insert or update operation on the model  
        context={ } #dict containing data to be sent to the client  

      return render(request, 'mytemplate.html', context) 