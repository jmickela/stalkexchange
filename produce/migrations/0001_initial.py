# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GardenItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(help_text='How many do you have?', verbose_name='Quantity', choices=[(0, 'A little'), (10, 'A lot')])),
                ('is_organic', models.BooleanField(default=False, verbose_name='Is Organic?')),
                ('size', models.IntegerField(help_text='How big is this item?', verbose_name='Size', choices=[(0, 'Big'), (1, 'Medium'), (2, 'Small')])),
                ('description', models.TextField(help_text='Extra information...', verbose_name='Description', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProduceType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='Type')),
                ('description', models.TextField(verbose_name='Description')),
            ],
        ),
        migrations.AddField(
            model_name='gardenitem',
            name='produce',
            field=models.ForeignKey(to='produce.ProduceType'),
        ),
    ]
