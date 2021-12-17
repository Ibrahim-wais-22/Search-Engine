from __future__ import unicode_literals
from typing import overload
from django.db import models



class Crawl_tb(models.Model):
    title = models.CharField(max_length=512)
    discraption =models.CharField(max_length=256)
    url = models.CharField(max_length=1024)

    def __unicode__(self):
        return "{} - {}".format(self.identifier,self.title)



class AddCommint(models.Model):
    name = models.CharField( max_length=50)
    email = models.EmailField(max_length=50)
    text = models.TextField(max_length=500)
    date = models.DateTimeField( auto_now=True)
    
    
    def __str__(self):
        return self.text
        

