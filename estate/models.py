from django.db import models

# Create your models here.
class Property(models.Model):
    prop_name = models.CharField(max_length=255)
    prop_price = models.BigIntegerField()
    prop_area = models.CharField(max_length=255)
    prop_beds = models.IntegerField()
    prop_bath = models.IntegerField()
    prop_garage = models.IntegerField()
    prop_image = models.ImageField(upload_to='pics')

class Agent(models.Model):
    agent_name = models.CharField(max_length=255)
    agent_tagline = models.CharField(max_length=255)
    agent_desc = models.TextField()
    agent_phone = models.BigIntegerField()
    agent_mobile = models.BigIntegerField()
    agent_email = models.EmailField()
    agent_skype = models.CharField(max_length=255)
    agent_image = models.ImageField(upload_to='pics',default=None)

class Contact(models.Model):
    name = models.CharField(max_length=225)
    email = models.EmailField()
    sub = models.CharField(max_length=225)
    msg = models.CharField(max_length=600)