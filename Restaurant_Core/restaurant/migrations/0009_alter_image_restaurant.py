# Generated by Django 4.1.2 on 2023-03-21 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0008_reservation_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='restaurant.restaurant'),
        ),
    ]
