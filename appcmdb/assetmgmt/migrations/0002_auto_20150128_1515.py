# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assetmgmt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domainname',
            name='BCP_server',
            field=models.ForeignKey(to='assetmgmt.BcpServers', blank=True),
        ),
    ]
