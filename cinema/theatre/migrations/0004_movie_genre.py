# Generated by Django 5.0.2 on 2024-02-20 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theatre', '0003_alter_movie_image_alter_user_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('none', 'None'), ('action', 'Action'), ('comedy', 'Comedy'), ('drama', 'Drama'), ('horror', 'Horror'), ('romance', 'Romance'), ('sci-fi', 'Science Fiction')], default='none', max_length=100),
        ),
    ]
