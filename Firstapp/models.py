from django.db import models




# Create your models here.
class persons(models.Model):
    Person_name = models.CharField(max_length=20)
    emailid =models.EmailField()
    phone =models.CharField(max_length=10)
    age = models.IntegerField()

    def __str__(self): 
        return f"{self.Person_name},{self.emailid}"
class Inputs(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)

    def __str__(self): 
        return f"{self.firstname},{self.lastname}" 
    
class Employee(models.Model):   
    name = models.CharField(max_length=100)   
    email = models.EmailField()   
    contact = models.CharField(max_length=15)   
    class Meta:   
        db_table = "Employee" 