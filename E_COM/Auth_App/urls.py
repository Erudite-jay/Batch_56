# /login
# /signup
# /resetpassword

#2
from django.urls import path
from . import views


urlpatterns=[
 path('home/',views.homepage),
 path('template-page/',views.temp_page)
 
]