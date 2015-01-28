# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assetmgmt', '0006_auto_20150128_1824'),
    ]

    operations = [
        migrations.CreateModel(
            name='DomainName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('domain_name', models.CharField(unique=True, max_length=255)),
                ('internal_ipaddr', models.IPAddressField()),
                ('bcp_ipaddr', models.IPAddressField(blank=True)),
                ('external_ipaddr', models.IPAddressField(blank=True)),
                ('BCP_server', models.ForeignKey(blank=True, to='assetmgmt.BcpServers', null=True)),
                ('app_software', models.ManyToManyField(to='assetmgmt.AppSoftware')),
                ('server', models.ForeignKey(to='assetmgmt.Servers')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u57df\u540d',
                'verbose_name_plural': '\u57df\u540d',
            },
            bases=(models.Model,),
        ),
    ]
