#-*- coding: utf-8 -*-

from django.db import models
#import datetime
#from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):              # __str__ on Python 3
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


    def __unicode__(self):              # __str__ on Python 3
        return self.choice_text



class Inges(models.Model):
    inges_text = models.CharField(max_length=200, verbose_name = "학교",)



    def __unicode__(self):              # __str__ on Python 3
        return self.inges_text