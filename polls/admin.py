#-*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from polls.models import Question, Choice, Inges


admin.site.register(Question)
admin.site.register(Choice)

admin.site.register(Inges)