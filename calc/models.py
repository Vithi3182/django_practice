from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.
class Destination(models.Model):
    
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc =RichTextField()
    price = models.IntegerField(default= 0.0)
    offer = models.BooleanField(default=False)

class Comments(models.Model):
    comment = models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    destination_name=models.ForeignKey(Destination,on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    like_count = models.PositiveIntegerField(default=0)
    liked_users = models.ManyToManyField(User, related_name='liked_comments', blank=True)
    
class IPViewTracking(models.Model):
    ip_address = models.GenericIPAddressField(unique=True)
    viewed_destinations = models.JSONField(default=list)

    def __str__(self):
        return self.ip_address