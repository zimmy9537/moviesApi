# Generated by Django 3.2.9 on 2021-12-29 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movielist_app', '0006_review_review_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='avg_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='number_rating',
            field=models.IntegerField(default=0),
        ),
    ]
