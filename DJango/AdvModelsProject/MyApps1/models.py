from django.db import models


# Create your models here.
class ContactInfo(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    address = models.CharField(max_length=256)

    class Meta:
        abstract = True  ##"ContactInfo" is base-model(Abstract-Base-Class)


class Student(ContactInfo):
    rollno = models.IntegerField()
    mark = models.IntegerField()


class Teacher(ContactInfo):
    subject = models.CharField(max_length=64)
    salary = models.FloatField()


class BasicModel(models.Model):  # base-class(not a abs-model-class)
    f1 = models.CharField(max_length=64)
    f2 = models.CharField(max_length=64)
    f3 = models.CharField(max_length=64)


class StandardModel(BasicModel):  # child-class
    f4 = models.CharField(max_length=64)
    f5 = models.CharField(max_length=64)


class Person(models.Model):
    name = models.CharField(max_length=64)
    age = models.IntegerField()


class Employee(Person):
    eno = models.IntegerField()
    esal = models.FloatField()


class Manager(Employee):
    exp = models.IntegerField()
    team_size = models.IntegerField()


class Parent1(models.Model):
    parent1_id = models.AutoField(primary_key=True)
    f1 = models.CharField(max_length=64)
    f2 = models.CharField(max_length=64)


class Parent2(models.Model):
    parent2_id = models.AutoField(primary_key=True)
    f3 = models.CharField(max_length=64)
    f4 = models.CharField(max_length=64)


class Child(Parent1, Parent2):
    f5 = models.CharField(max_length=64)
    f6 = models.CharField(max_length=64)


class Employees(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=64)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=256)
