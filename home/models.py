from django.db import models
from django.contrib.auth.models import User
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


class UserProfile(models.Model):
    GENDER_CHOICES = (
        ("MALE","male"),
        ("FEMALE","female"),
        ("OTHERS","others"),
    )
    UserUsername = models.OneToOneField(User,on_delete=models.CASCADE,blank=True, null=True)
    phoneNumber = models.CharField(blank=True,null=True,max_length=12)
    Gender = models.CharField(choices=GENDER_CHOICES,max_length=50,blank=True)
    Dob = models.DateField(auto_now_add=False,auto_now=False,blank=True,null=True)
    JoiningDate = models.DateTimeField(auto_now=True)
    Country = models.CharField(max_length=100,blank=True, null=True)
    State = models.CharField(max_length=100,blank=True, null=True)
    District = models.CharField(max_length=100,blank=True, null=True)
    city = models.CharField(max_length=100,blank=True, null=True)
    address = models.CharField(max_length=100,blank=True, null=True)
    designation = models.CharField(max_length=100,blank=True, null=True)
    facebook_url = models.CharField(max_length=100,blank=True, null=True)
    instagram_url = models.CharField(max_length=100,blank=True, null=True)
    twitter_url = models.CharField(max_length=100,blank=True, null=True)
    pincode = models.CharField(blank=True,null=True,max_length=10)
    Bio = models.TextField(blank=True, null=True)
    coverImage = models.ImageField(blank=True, null=True,upload_to='images/coverImage/',default='defaultCover.jpg')
    profileImage = models.ImageField(blank=True, null=True,upload_to='images/profileImage/',default='defaultProfile.jpg')
    isPublic = models.BooleanField(default=False)
    securityQues = models.CharField(max_length=200,blank=True, null=True)
    securityAns = models.CharField(max_length=400,blank=True, null=True)
    language = models.CharField(max_length=400,blank=True, null=True)

    def __str__(self):
        return str(self.UserUsername)