# Generated by Django 5.0.3 on 2024-05-10 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0009_filmdetails_ratings'),
    ]

    operations = [
        migrations.AddField(
            model_name='filmdetails',
            name='video_shortDesc',
            field=models.TextField(default='video short description', max_length=50),
        ),
        migrations.AlterField(
            model_name='filmdetails',
            name='video_desc',
            field=models.TextField(max_length=50),
        ),
    ]
