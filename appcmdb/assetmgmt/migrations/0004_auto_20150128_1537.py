# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assetmgmt', '0003_auto_20150128_1520'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bcpservers',
            options={'ordering': ['id'], 'verbose_name': 'BCP\u670d\u52a1\u5668', 'verbose_name_plural': 'BCP\u670d\u52a1\u5668'},
        ),
        migrations.AlterModelOptions(
            name='servers',
            options={'ordering': ['id'], 'verbose_name': '\u670d\u52a1\u5668', 'verbose_name_plural': '\u670d\u52a1\u5668'},
        ),
        migrations.AlterField(
            model_name='domainname',
            name='internal_ipaddr',
            field=models.IPAddressField(unique=True, blank=True),
        ),
    ]
