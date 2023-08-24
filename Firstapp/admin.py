from django.contrib import admin

from .models import Inputs,persons
# Register your models here.
 
admin.site.register(persons)

#admin.site.register(Inputs)

@admin.register(Inputs) 
class PersonAdmin(admin.ModelAdmin): 
    search_fields = ("first_name__startswith", ) 
