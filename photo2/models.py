from django.db import models
# Create your models here.
class nature(models.Model):
    image = models.ImageField(upload_to='images/nature') 
class bird(models.Model):
    image = models.ImageField(upload_to='images/bird')
class reptile(models.Model):
    image = models.ImageField(upload_to='images/reptile')
class insects(models.Model):             
    image = models.ImageField(upload_to='images/insect')
class travels(models.Model):    
    image = models.ImageField(upload_to='images/travel')    