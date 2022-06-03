from django.db import models
# from hitcount.models import HitCountMixin, HitCount
# from django.contrib.contenttypes.fields import GenericRelation

from django.core.validators import FileExtensionValidator
from django.db.models import CASCADE, SET_NULL
from django.utils.text import slugify
from django.conf import settings
from django.contrib.auth.models import User
import uuid
import os
# Create your models here.

class UserContactMessage(models.Model):
    user = models.ForeignKey(User, related_name='user_contact_us', on_delete=CASCADE)
    name = models.CharField(max_length=100,blank=True, null=True)
    email = models.CharField(max_length=100,blank=True, null=True)
    subject = models.CharField(max_length=100,blank=True, null=True)
    message=models.TextField(max_length=2000,blank=True, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(blank=True, auto_now=True, null=True)



class Product(models.Model):
    name=models.CharField(max_length=200)
    desc=models.TextField()
    image=models.ImageField()
    price=models.BigIntegerField()

    # print(request.user.username)


    def save(self,*args,**kwrgs):
        #do some task during save any object
        print(request.user)
        return super(Product,self).save(*args,**kwrgs)