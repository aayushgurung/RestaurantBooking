# Generated by Django 4.1.2 on 2023-05-03 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0024_userprofile_last_rated_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='user',
            new_name='user_id',
        ),
    ]
