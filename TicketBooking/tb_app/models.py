from django.db import models


class Payment(models.Model):
    Emailcard = models.CharField(max_length=200)
    Cardnumber = models.CharField(max_length=100)
    Expirycard = models.CharField(max_length=100)
    CVVcard = models.CharField(max_length=100)
    NameCard = models.CharField(max_length=100)

class CustomerLogin(models.Model):

    
    Password = models.CharField(max_length=100)

    UserName = models.CharField(max_length=100)

class CustomerSignup(models.Model):

    Email = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Password2 = models.CharField(max_length=100)
    UserName = models.CharField(max_length=100)
