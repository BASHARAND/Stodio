# Generated by Django 3.2.9 on 2022-02-02 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('silling', '0012_auto_20220127_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albums',
            name='Hasbands',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='albums',
            name='Size',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='albums',
            name='Type',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='albums',
            name='Write',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
