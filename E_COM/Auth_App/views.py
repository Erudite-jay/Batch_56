from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from .models import Contact
from . serializers import ContactSerializer

import json

from django.views.decorators.csrf import csrf_exempt

# Create your views here.

#3
def homepage(request):
    return HttpResponse("Hello world !! ")

def temp_page(request):
    return render(request,"Auth_App/index.html")

@csrf_exempt
def contact_data(request):
    if request.method =="GET":

        all_users=Contact.objects.all() #queryset

        sd=ContactSerializer(all_users,many=True) #serilized data
    
        return JsonResponse({
            "success":True,
            "Data":sd.data
        }, status=200)
    
    if request.method=="POST":

        input_data=json.loads(request.body) #json data from the client side

        sd=ContactSerializer(data=input_data) #Deserailized data

        if sd.is_valid():
            sd.save()

            return JsonResponse({
            "success":True,
            "Data":sd.data
        }, status=201)


@csrf_exempt
def single_user_data(request, pk):
    if request.method=="GET":
        try:
            user=Contact.objects.get(pk=pk) #finding single user using pk
            sd=ContactSerializer(user) #serializing data

            return JsonResponse({
                "success":True,
                "Data":sd.data
            }, status=200)
        
        except Exception as e:
            return JsonResponse({
                "success":False,
                "Data":sd.data
            }, status=500)
        

    if request.method=="PUT":
        try:
            user=Contact.objects.get(pk=pk)
            input_data=json.loads(request.body)
            sd=ContactSerializer(user,data=input_data)
            if sd.is_valid():
                sd.save()
                return JsonResponse({
                "success":True,
                "Data":sd.data,
                "Message":"Data updated successfully"
            }, status=200)

        except Exception as e:
            return JsonResponse({
                "success":False,
                "Data":sd.data
            }, status=500)

    if request.method=="PATCH":
        try:
            user=Contact.objects.get(pk=pk)
            input_data=json.loads(request.body)
            sd=ContactSerializer(user,data=input_data, partial=True)

            if sd.is_valid():
                sd.save()
                return JsonResponse({
                "success":True,
                "Data":sd.data,
                "Message":"Data updated successfully"
            }, status=200)
            else:
                return JsonResponse({
                "success":False,
                "error":sd.errors
            }, status=400)

        except Exception as e:
            return JsonResponse({
                "success":False,
                "Data":sd.data,
                "Error":str(e)
            }, status=500)
    
    if request.method=="DELETE":
        user=Contact.objects.get(pk=pk)
        user.delete()

        return JsonResponse({
                "success":True,
                "Message":"Data deleted successfully",
            }, status=200)
