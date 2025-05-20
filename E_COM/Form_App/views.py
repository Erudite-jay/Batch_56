from django.http import JsonResponse
from django.shortcuts import render
from .forms import FileUploadFormClass
from .models import FileUpload
# Create your views here.

def file_upload_form(request):
    if request.method=="POST":
        form=FileUploadFormClass(request.POST,request.FILES) #form data

        if form.is_valid():
            #if you are using model form
            form.save()
            
            #if you are using normal form
            # record=FileUpload(name=form.cleaned_data['name'],file=form.cleaned_data['file'])
            # record.save()
            return JsonResponse({
                "success":True,
                "sessage":"File uploaded successfully"
            })
   
    else:
        form =FileUploadFormClass() #empty form 
        print(form)

    return render(request,"Form_App/file_upload.html",{"form":form})