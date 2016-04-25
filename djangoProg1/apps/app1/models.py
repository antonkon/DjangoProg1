from django.db import models

# Create your models here.
class Interview(models.Model):
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    text = models.CharField()
    date = models.DateField(auto_now_add=True)