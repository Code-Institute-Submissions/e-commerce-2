# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-09 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='World',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(default='', max_length=254)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
