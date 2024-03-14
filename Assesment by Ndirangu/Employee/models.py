from django.db import models


# Create your models here.
class Employee(models.Model):
    fullname = models.CharField,
    email = models.EmailField,
    employee_id = models.CharField,
    id_no = models.CharField,
    phone_no = models.CharField,

    def __str__(self):
        return self.fullname


class registration(models.Model):
    Firstname = models.CharField,
    lastname = models.CharField,
    Phone_no = models.CharField,
    Password = models.CharField,

    def __str__(self):
        return self.Firstname
