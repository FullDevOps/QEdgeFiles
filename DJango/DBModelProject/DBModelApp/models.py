from django.db import models

# Create your models here.
class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=30)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=30)

    def __str__(self):
        return 'Employee Object with eno: ' + str(self.eno);


class Company(models.Model):
    compid= models.IntegerField();
    compname=models.CharField(max_length=50);
    noofemps=models.IntegerField();
    compaddr=models.CharField(max_length=100);
    compsharevalue = models.FloatField();