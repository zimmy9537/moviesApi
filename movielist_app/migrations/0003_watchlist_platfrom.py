# Generated by Django 3.2.9 on 2021-11-27 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movielist_app', '0002_auto_20211127_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='platfrom',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='watchlist', to='movielist_app.streamplatform'),
            preserve_default=False,
        ),
    ]
