# Generated by Django 4.0.1 on 2022-01-13 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0003_remove_movierecord_movie_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='movierecord',
            name='udata',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]
