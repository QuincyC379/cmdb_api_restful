# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-07-03 06:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0002_plansserver_orgid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='networkdevice',
            old_name='intranet_ip',
            new_name='int_ip',
        ),
        migrations.AddField(
            model_name='networkdevice',
            name='ext_ip',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='外网IP'),
        ),
    ]
