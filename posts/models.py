from django.db import models
from django.contrib.auth.models import User


class UserPost(models.Model):
    content = models.CharField(max_length=512)
    pub_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
