# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-07-03 06:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0004_remove_networkdevice_vlan_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='networkdevice',
            name='note',
            field=models.CharField(max_length=128, null=True, verbose_name='备注'),
        ),
    ]
