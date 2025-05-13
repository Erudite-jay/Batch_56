from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#3
def homepage(request):
    return HttpResponse("Hello world !! ")

def temp_page(request):
    return render(request,"Auth_App/index.html")