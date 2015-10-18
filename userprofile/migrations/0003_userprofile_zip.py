# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_auto_20151017_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='zip',
            field=models.CharField(help_text='Your zip code is used to keep search results local', max_length=5, verbose_name='Zip Code', blank=True),
        ),
    ]
