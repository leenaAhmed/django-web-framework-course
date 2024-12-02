from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')



def myview(request):  

      if request.method=='GET':  
        val = request.GET['key'] 
            #perform read or delete operation on the model  

      if request.method=='POST':  
        #perform insert or update operation on the model  
        context={ } #dict containing data to be sent to the client  

      return render(request, 'mytemplate.html', context) 