from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    full_name = models.CharField(max_length=264, blank=True)
    description = models.TextField(blank=True)
    dob = models.DateField(blank=True, null=True)
    websile = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    def __str__(self):
        return self.user

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    Created_date = models.DateTimeField(auto_now_add=True)
