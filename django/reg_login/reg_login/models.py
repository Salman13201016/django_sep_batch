from django.db import models


class User(models.Model):
    name = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    pw = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    v_code = models.CharField(max_length=500,unique=True)
    v_status = models.CharField(max_length=500)
    