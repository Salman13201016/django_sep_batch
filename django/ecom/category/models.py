from django.db import models

# Create your models here.

class Categories(models.Model):
    cat_name = models.CharField(max_length = 500)
    cat_code = models.CharField(max_length = 500)
