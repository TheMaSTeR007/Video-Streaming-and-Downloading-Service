# Generated by Django 5.0.3 on 2024-05-10 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0008_remove_filmdetails_ratings_filmdetails_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='filmdetails',
            name='ratings',
            field=models.IntegerField(default=0),
        ),
    ]
