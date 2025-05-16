# /login
# /signup
# /resetpassword

#2
from django.urls import path
from . import views


urlpatterns=[
 path('home/',views.homepage),
 path('template-page/',views.temp_page),

 path('contact-data/',views.contact_data),
 
 path('sud/<int:pk>/',views.single_user_data)
]