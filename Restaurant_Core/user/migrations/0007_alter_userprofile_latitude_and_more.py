# Generated by Django 4.1.2 on 2023-04-08 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_userprofile_latitude_userprofile_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='latitude',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='longitude',
            field=models.IntegerField(default=0, null=True),
        ),
    ]