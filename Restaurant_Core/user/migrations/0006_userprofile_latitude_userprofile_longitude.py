# Generated by Django 4.1.2 on 2023-04-08 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_ownerrestaurant'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='latitude',
            field=models.IntegerField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='longitude',
            field=models.IntegerField(default=False),
        ),
    ]
