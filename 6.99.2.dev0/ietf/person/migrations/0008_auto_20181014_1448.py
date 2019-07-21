# Copyright The IETF Trust 2018-2019, All Rights Reserved
# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-14 14:48


from __future__ import absolute_import, print_function, unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0007_auto_20180929_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalapikey',
            name='endpoint',
            field=models.CharField(choices=[(b'/api/iesg/position', b'/api/iesg/position'), (b'/api/v2/person/person', b'/api/v2/person/person'), (b'/api/meeting/session/video/url', b'/api/meeting/session/video/url')], max_length=128),
        ),
    ]
