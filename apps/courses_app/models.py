# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class CourseManager(models.Manager):
    def no_blank_field(self, postData):
        error = []
        if postData['name'] == "" or postData['description'] == "":
            error.append("no blank entry")
            print error

        if len(error) ==0:
            d =  Course.objects.create(name=postData['name'], description=postData['description'])
            return [True, d]
        else:
            return [False, False]
            
    def remove_course(self, id):
        Course.objects.get(id=id).delete()


class Course(models.Model):
     name = models.CharField(max_length=38)
     description = models.CharField(max_length=38)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     objects = CourseManager()

     def __unicode__(self):
         return "id: " + str(self.id) + ", name: " + self.name + ", description: " + self.description + ", add_date: " + str(self.created_at)
