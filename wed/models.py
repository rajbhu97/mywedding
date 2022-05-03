from django.db import models

# Create your models here.
class RequestModel(models.Model):
  name = models.CharField(max_length = 15)
  email = models.CharField(max_length = 35)
  guests = models.CharField(max_length = 30)
  message = models.CharField(max_length = 100)
  
  def __str__(self):
    return f"My name is '{self.name}' and my message '{self.message}' "

class Song(models.Model):
  song = models.FileField(upload_to ='media/song/' ,blank = True, null = True)
  
class Rajesh(models.Model):
  rajesh = models.FileField(upload_to ='media/rajesh/' ,blank = True, null = True)
  
class Bhuvana(models.Model):
  bhuvana = models.FileField(upload_to ='media/bhuvana/' ,blank = True, null = True)
  
