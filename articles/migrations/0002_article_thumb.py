# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-18 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumb',
            field=models.ImageField(blank=True, default='dafault.png', upload_to=b''),
        ),
    ]
