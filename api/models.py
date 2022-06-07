from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Device(models.Model):
    deviceId=models.CharField(max_length=10,primary_key=True)
    deviceType=models.CharField(max_length=20)
    lightStatus1=models.IntegerField(choices=((0,0),(1,1)),default=0)
    lightStatus2=models.IntegerField(choices=((0,0),(1,1)),default=0)
    lightStatus3=models.IntegerField(choices=((0,0),(1,1)),default=0)
    lightStatus4=models.IntegerField(choices=((0,0),(1,1)),default=0)
    def __str__(self):
        return self.deviceId

class UserDevice(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    device=models.ForeignKey(Device,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + ' ' + self.device.deviceId
