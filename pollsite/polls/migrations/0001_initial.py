# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
        migrations.CreateModel(
            name='AdvancedChoice',
            fields=[
                ('choice_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='polls.Choice')),
                ('weight', models.IntegerField(default=10)),
            ],
            options={
                'abstract': False,
            },
            bases=('polls.choice',),
        ),
        migrations.AddField(
            model_name='choice',
            name='polymorphic_ctype',
            field=models.ForeignKey(related_name='polymorphic_polls.choice_set+', editable=False, to='contenttypes.ContentType', null=True),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(to='polls.Question'),
        ),
    ]
