from django.db import models
from django.utils import timezone
# Create your models here.
class SecurityQuestion(models.Model):
    question = models.CharField(max_length=200)

    def __str__(self) :
        return self.question

class Register(models.Model):
        fname = models.CharField(max_length=100,default='')
        lname = models.CharField(max_length=100,default='')
        phone = models.CharField(max_length=10,default='',null=True,blank=True)
        email = models.EmailField(max_length=200,default='')
        companyName = models.CharField(max_length=200,default='',null=True,blank=True)
        securityQuestion = models.CharField(max_length=200,default='',null=True,blank=True)
        securityAnswer = models.CharField(max_length=200,default='',null=True,blank=True)
        password = models.CharField(max_length=200,default='',null=True,blank=True)
        pin = models.CharField(max_length=100,default='',null=True,blank=True)
        token = models.CharField(max_length=200,default='',null=True,blank=True)
        status = models.CharField(max_length=10,default='0')
        addedDate = models.DateTimeField(default=timezone.now)
        modifyDate = models.DateTimeField(default=timezone.now)
        
def __str__(self) :
        return self.fname

        
class PasswordHistory(models.Model):
        password = models.CharField(max_length=100)
        userId = models.IntegerField()
        modifyDate = models.DateTimeField(default=timezone.now)
        
def __str__(self) :
        return self.password

class Device(models.Model):
        deviceName = models.CharField(max_length=100)
        macId = models.CharField(max_length=100)
        deviceId = models.CharField(max_length=10)
        userId = models.CharField(max_length=10,default='')
        
def __str__(self) :
        return self.deviceName