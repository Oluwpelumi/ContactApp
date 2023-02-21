from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    relationship =  models.CharField(max_length=50)
    phone_number =  models.CharField(max_length=50)
    address =  models.CharField(max_length=100)
    email =  models.EmailField(max_length=254)

    def __str__(self):
        return self.full_name 