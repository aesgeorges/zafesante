# Generated by Django 2.0.1 on 2018-03-15 18:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ['created']},
        ),
        migrations.AddField(
            model_name='video',
            name='created',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='video',
            name='name',
            field=models.CharField(default='vid', max_length=255),
        ),
        migrations.AddField(
            model_name='video',
            name='slug',
            field=models.SlugField(default='slug', max_length=255, unique=True),
        ),
    ]
