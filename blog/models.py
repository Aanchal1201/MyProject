from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class UserPost(models.Model):
    authorUsername = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    label = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/userPost/')
    slug = models.CharField(max_length=255)
    author = models.CharField(max_length=50)
    timeStamp = models.DateTimeField()
    # dateUpdates = models.IntegerField()
    timeRead = models.CharField(max_length=10)
    content = RichTextField(blank=True)
    userStatus = models.CharField(max_length=50)
    adminStatus = models.BooleanField(default=False)

    def __str__(self):
        return self.title