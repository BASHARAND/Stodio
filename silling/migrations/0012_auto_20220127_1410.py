# Generated by Django 3.2.9 on 2022-01-27 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('silling', '0011_auto_20220110_1940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='write',
            name='file',
        ),
        migrations.AlterField(
            model_name='albums',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='media'),
        ),
    ]
