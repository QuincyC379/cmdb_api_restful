# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-07-03 06:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0003_auto_20170703_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='networkdevice',
            name='vlan_ip',
        ),
    ]
