# Generated by Django 3.2.9 on 2021-11-26 17:12

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('silling', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Size', models.CharField(blank=True, max_length=10, null=True)),
                ('Form', models.CharField(blank=True, max_length=10, null=True)),
                ('Type', models.CharField(blank=True, max_length=10, null=True)),
                ('Color', colorfield.fields.ColorField(default='#FF0000', max_length=18)),
            ],
        ),
    ]
