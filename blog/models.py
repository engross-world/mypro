from django.db import models
from users.models import Adduser
from datetime import datetime 
from django.utils import timezone

# Create your models here.
class Addblog(models.Model):
    title =models.CharField(max_length=200)
    post = models.TextField(max_length=2000)
    user = models.ForeignKey(to=Adduser,on_delete=models.CASCADE)
    #If user delete for the main table its will delete for the child table too 
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return(f"{self.user}")


