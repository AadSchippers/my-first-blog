# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-10 12:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_loginstatus'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LoginStatus',
        ),
    ]