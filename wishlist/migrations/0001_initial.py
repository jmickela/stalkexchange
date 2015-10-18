# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('produce', '0002_gardenitem_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='WishlistItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('owner', models.ForeignKey(related_name='wishlist_items', to=settings.AUTH_USER_MODEL)),
                ('produce', models.ForeignKey(to='produce.ProduceType')),
            ],
        ),
    ]
