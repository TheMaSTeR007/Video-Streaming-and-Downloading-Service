# Generated by Django 5.0.1 on 2024-04-22 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FilmDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_field', models.CharField(max_length=100)),
                ('video_desc', models.TextField()),
                ('duration', models.CharField(max_length=20)),
                ('released_date', models.DateField()),
            ],
        ),
    ]
