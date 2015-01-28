# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assetmgmt', '0009_domainname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='domainname',
            name='app_software',
        ),
    ]
