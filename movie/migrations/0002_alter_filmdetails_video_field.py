# Generated by Django 5.0.1 on 2024-04-22 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmdetails',
            name='video_field',
            field=models.FileField(upload_to='static/media'),
        ),
    ]
