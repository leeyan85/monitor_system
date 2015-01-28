# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assetmgmt', '0007_domainname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='domainname',
            name='BCP_server',
        ),
        migrations.RemoveField(
            model_name='domainname',
            name='app_software',
        ),
        migrations.RemoveField(
            model_name='domainname',
            name='server',
        ),
        migrations.DeleteModel(
            name='DomainName',
        ),
    ]
