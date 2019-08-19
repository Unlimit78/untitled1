from django.db import models
from main.models import AdvUser

class FindFriend(models.Model):
    find = models.CharField(max_length=200,verbose_name='Find')
    class Meta:
        pass

class Friend(models.Model):
    to_user = models.ForeignKey(AdvUser,related_name='friends',on_delete=models.CASCADE)
    from_user = models.ForeignKey(AdvUser,on_delete=models.PROTECT)