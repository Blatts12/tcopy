from django.db import models
from accounts.models import CustomUser


class UserPost(models.Model):
    content = models.CharField(max_length=512)
    pub_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
