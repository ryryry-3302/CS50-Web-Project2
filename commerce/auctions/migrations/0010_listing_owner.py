# Generated by Django 4.0.4 on 2022-05-20 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_watchlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='owner',
            field=models.CharField(blank=True, max_length=400),
        ),
    ]