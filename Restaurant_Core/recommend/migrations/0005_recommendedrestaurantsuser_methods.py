# Generated by Django 4.1.2 on 2023-05-04 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0004_recommendedrestaurantsuser_distance'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendedrestaurantsuser',
            name='methods',
            field=models.CharField(default='ratings', max_length=10),
            preserve_default=False,
        ),
    ]