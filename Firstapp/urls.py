from django.http import HttpRequest
from django.urls import path

from . import views
from .forms import *


urlpatterns = [
    path('', views.view, name='view'),
    path('response',views.test,name='response'),
    path ('homeview', views.form_view , name = 'homeview'),
    path('about', views.about , name='about'),
    path('create/', EmployeeCreate.as_view(), name = 'EmployeeCreate'), 
    path('employees/success/', SuccessView.as_view(), name='success'),
    path('/employees/delete/',delete_view.as_view(), name = "deleteview"),
    path('list', EmployeeList.as_view(), name='list'),
    path('show/<int:pk>', EmployeeDetail.as_view(), name = 'EmployeeDetail'),
    path('update/<int:pk>', EmployeeUpdate.as_view(), name = 'EmployeeUpdate'),
    path('delete/<int:pk>', EmployeeDelete.as_view(), name = 'EmployeeDelete'),
]