from django.db import models
from django.contrib.auth.models import AbstractUser



class AdvUser(AbstractUser):
    is_activated = models.BooleanField(default=True,db_index=True,verbose_name='Activated ?')
    send_messages = models.BooleanField(default=True,verbose_name='Send messages ?')
    model_pic = models.ImageField(upload_to='media/',default='media/default.png',blank=True,verbose_name='Image')
    date_of_birth = models.DateField(default='2000-08-29',blank=True)
    about = models.TextField(default='',blank=True)
    Hobbys = models.TextField(default='',blank=True)

    class Meta:
        pass

class Photos(models.Model):
    location = models.ForeignKey('AdvUser',related_name='photos',on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='media/',blank=True,default='',verbose_name='photo')


