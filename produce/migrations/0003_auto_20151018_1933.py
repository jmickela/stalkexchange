# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produce', '0002_gardenitem_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='gardenitem',
            name='image',
            field=models.ImageField(upload_to=b'', verbose_name='Image', blank=True),
        ),
        migrations.AddField(
            model_name='producetype',
            name='image',
            field=models.ImageField(upload_to=b'', verbose_name='Image', blank=True),
        ),
    ]
