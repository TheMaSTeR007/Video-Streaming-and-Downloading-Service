# Generated by Django 5.0.3 on 2024-05-12 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0015_remove_bollywood_duration_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmdetails',
            name='video_field',
            field=models.FileField(max_length=500, upload_to='static/media/AllFilms'),
        ),
    ]