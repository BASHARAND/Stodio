# Generated by Django 3.2.9 on 2021-12-30 10:09

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('silling', '0004_auto_20211129_1611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='type',
            name='Type',
        ),
        migrations.AddField(
            model_name='type',
            name='Color',
            field=colorfield.fields.ColorField(default='#FF0000', max_length=18),
        ),
    ]
