# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-02 18:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appella', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='us_imagen',
            new_name='us_img',
        ),
    ]
