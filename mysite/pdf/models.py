from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.TextField()
    summmary = models.TextField()
    school = models.TextField()
    university = models.TextField()
    previous_work = models.TextField()
    skills = models.TextField()
    

