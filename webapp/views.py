from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request,'Myapp/homepage.html')
def register_form(request):
    return render(request,'Myapp/signup from.html')
