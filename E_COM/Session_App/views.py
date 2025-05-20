from django.http import JsonResponse
from django.shortcuts import render
from . models import User
# Create your views here.

def login_view(request):
    if request.session.get('username'):
        return JsonResponse({
            "success":True,
            "message":"User already logged in",
            "user is": request.session.get('username')
        })
    
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        current_user=User.objects.get(username=username)

        if current_user.password==password:
            request.session.set_expiry(20)
            request.session['username']=username
            return JsonResponse({
                "success":True,
                "message":"Login successfully"
            })
    return render(request, "Session_App/loginPage.html")