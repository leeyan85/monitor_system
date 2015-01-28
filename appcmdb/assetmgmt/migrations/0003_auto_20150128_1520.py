# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assetmgmt', '0002_auto_20150128_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domainname',
            name='BCP_server',
            field=models.ForeignKey(blank=True, to='assetmgmt.BcpServers', null=True),
        ),
    ]
