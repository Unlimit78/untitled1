from django.db import models
from main.models import  AdvUser

class Dialog(models.Model):
    members = models.ManyToManyField(AdvUser)

class Message(models.Model):
    message = models.TextField(null=True)
    chat = models.ForeignKey(Dialog,on_delete=models.CASCADE)
    author = models.ForeignKey(AdvUser,on_delete=models.CASCADE,null=True)
    is_readed = models.BooleanField(default=False)
