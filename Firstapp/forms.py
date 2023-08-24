from django import forms
from .models import Inputs,Employee
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView 
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView


class Inputforms(forms.ModelForm):
    class Meta:
        model = Inputs
        #fields = ['name', 'email', 'phone', 'message'] we can use instead of 
        fields = '__all__'

class EmployeeCreate(CreateView):   
    model = Employee    
    fields = '__all__' 
    template_name = 'employeeCreate.html'  # Update this line
    success_url = "/employees/success/" 
    
class SuccessView(TemplateView):
    template_name = 'success.html'  

class delete_view(TemplateView):
    template_name ='Delete.html '

class EmployeeList(ListView):   
    model = Employee   
    success_url = "/employees/success/" 

class EmployeeDetail(DetailView):
    model = Employee    
    fields = '__all__' 

class EmployeeUpdate(UpdateView):
    model = Employee
    fields = '__all__'
    template_name = 'employeeUpdate.html'  #
    success_url = "/employees/success/" 

class EmployeeDelete(DeleteView):
    model = Employee
    success_url = "/employees/delete/"

    