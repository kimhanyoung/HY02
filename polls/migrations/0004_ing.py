# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 05:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_remove_choice_vote'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ing_text', models.CharField(max_length=200)),
            ],
        ),
    ]
