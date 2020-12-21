from django.db import models

# Create your models here.
class Adduser(models.Model):
    fullname = models.CharField(max_length = 100)
    email = models.EmailField(max_length=200,unique=True) #for primary key -> primary_key = True
    password = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.email}"
        #return f"{self.fullname},{self.email}"