from django.db import models

# Create your models here.

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    desc = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return (str(self.timeStamp)[0:19] +  " " + self.name)