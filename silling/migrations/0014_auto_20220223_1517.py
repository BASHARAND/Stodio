# Generated by Django 3.2.9 on 2022-02-23 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('silling', '0013_auto_20220202_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='albums',
            name='Colorw',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='albums',
            name='Countp',
            field=models.IntegerField(default=10),
        ),
    ]