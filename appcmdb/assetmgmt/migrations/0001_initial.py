# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppSoftware',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=10)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u5e94\u7528\u8f6f\u4ef6',
                'verbose_name_plural': '\u5e94\u7528\u8f6f\u4ef6',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BCPIPaddrs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ipaddr', models.IPAddressField(unique=True)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'BCPIP',
                'verbose_name_plural': 'BCPIP',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BcpServers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostname', models.CharField(unique=True, max_length=255)),
                ('bcp_ipaddr', models.ManyToManyField(to='assetmgmt.BCPIPaddrs')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'BCP\u670d\u52a1\u5668',
                'verbose_name_plural': 'BCP\u670d\u52a1\u5668',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DataCenter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u673a\u623f',
                'verbose_name_plural': '\u673a\u623f',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DomainName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('domain_name', models.CharField(unique=True, max_length=255)),
                ('bcp_ipaddr', models.ForeignKey(to='assetmgmt.BCPIPaddrs', blank=True)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u57df\u540d',
                'verbose_name_plural': '\u57df\u540d',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=10)),
                ('desc', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u670d\u52a1\u7ec4',
                'verbose_name_plural': '\u670d\u52a1\u7ec4',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IPaddrs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ipaddr', models.IPAddressField(unique=True)),
                ('DMZ', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'IP',
                'verbose_name_plural': 'IP',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServerLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=10)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u670d\u52a1\u7ea7\u522b',
                'verbose_name_plural': '\u670d\u52a1\u7ea7\u522b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Servers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostname', models.CharField(unique=True, max_length=255)),
                ('vitual_machine', models.BooleanField(default=True)),
                ('memory', models.CharField(max_length=20)),
                ('cpu', models.SmallIntegerField()),
                ('app_software', models.ManyToManyField(to='assetmgmt.AppSoftware')),
                ('bcpserver', models.OneToOneField(null=True, blank=True, to='assetmgmt.BcpServers')),
                ('group', models.ForeignKey(to='assetmgmt.Groups')),
                ('ip_addrs', models.ManyToManyField(to='assetmgmt.IPaddrs')),
                ('level', models.ForeignKey(to='assetmgmt.ServerLevel')),
                ('location', models.ForeignKey(to='assetmgmt.DataCenter')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u670d\u52a1\u5668',
                'verbose_name_plural': '\u670d\u52a1\u5668',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServiceLines',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20)),
                ('group', models.ManyToManyField(to='assetmgmt.Groups')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u4e1a\u52a1\u7ebf',
                'verbose_name_plural': '\u4e1a\u52a1\u7ebf',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='servers',
            name='serviceline',
            field=models.ForeignKey(to='assetmgmt.ServiceLines'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='domainname',
            name='internal_addr',
            field=models.ForeignKey(to='assetmgmt.IPaddrs'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bcpservers',
            name='location',
            field=models.ForeignKey(to='assetmgmt.DataCenter'),
            preserve_default=True,
        ),
    ]
