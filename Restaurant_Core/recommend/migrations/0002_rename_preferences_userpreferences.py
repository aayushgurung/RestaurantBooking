# Generated by Django 4.1.2 on 2023-04-08 10:29

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurant', '0011_alter_reservation_restaurant'),
        ('recommend', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='preferences',
            new_name='UserPreferences',
        ),
    ]
