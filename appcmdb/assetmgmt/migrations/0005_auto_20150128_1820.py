# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assetmgmt', '0004_auto_20150128_1537'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='domainname',
            name='app_software',
        ),
        migrations.AddField(
            model_name='servers',
            name='app_software',
            field=models.ManyToManyField(to='assetmgmt.AppSoftware'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='domainname',
            name='domain_name',
            field=models.CharField(unique=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='domainname',
            name='internal_ipaddr',
            field=models.IPAddressField(),
        ),
    ]
