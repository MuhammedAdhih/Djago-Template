from django.shortcuts import render

# Create your views here.


def home(request):
    context = {
        'name' : 'john',
        'course' : 'django',
        'is_loggedIn' : True
    }
    
    return render(request,'home.html',context)

def about(request):
    return render (request , 'about.html')

def products (request):
    return render (request,'products.html')