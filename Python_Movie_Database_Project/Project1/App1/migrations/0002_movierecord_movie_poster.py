# Generated by Django 4.0.1 on 2022-01-11 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movierecord',
            name='Movie_poster',
            field=models.ImageField(default='exit', upload_to='media/'),
            preserve_default=False,
        ),
    ]
