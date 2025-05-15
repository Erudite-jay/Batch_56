from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from .models import Contact
from . serializers import ContactSerializer

# Create your views here.

#3
def homepage(request):
    return HttpResponse("Hello world !! ")

def temp_page(request):
    return render(request,"Auth_App/index.html")

def contact_data(request):
    if request.method =="GET":

        all_users=Contact.objects.all() #queryset

        sd=ContactSerializer(all_users,many=True) #serilized data
    
        return JsonResponse({
            "success":True,
            "Data":sd.data
        }, status=200)

