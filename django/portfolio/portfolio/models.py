from django.db import models

class About(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 500)
    email = models.CharField(max_length = 500,unique=True)
    phone = models.CharField(max_length = 500)
    dob = models.CharField(max_length = 500)
    git = models.CharField(max_length = 500)
    fb = models.CharField(max_length = 500)
    linkedin = models.CharField(max_length = 500)
    pw = models.CharField(max_length = 500)
    gender = models.CharField(max_length = 500)
    address = models.CharField(max_length = 500)
    description = models.CharField(max_length = 500)

class Facts(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length = 500)
    no_of_client = models.CharField(max_length = 500)
    no_of_project = models.CharField(max_length = 500)
    no_of_hours = models.CharField(max_length = 500)
    no_of_hardworkers = models.CharField(max_length = 500)
    

    