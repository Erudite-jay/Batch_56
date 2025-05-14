from django.contrib import admin
from . models import Contact,Test
# Register your models here.

# admin.site.register(Contact)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=['id','name','phone','message']
    search_fields=['name','phone','message']
    list_filter=['name','id']

admin.site.register(Test)

