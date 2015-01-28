# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assetmgmt', '0005_auto_20150128_1820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='domainname',
            name='BCP_server',
        ),
        migrations.RemoveField(
            model_name='domainname',
            name='server',
        ),
        migrations.DeleteModel(
            name='DomainName',
        ),
    ]
