# Generated by Django 4.0.4 on 2022-05-21 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_alter_bid_winner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='open',
        ),
        migrations.AddField(
            model_name='listing',
            name='open',
            field=models.BooleanField(default='True'),
        ),
    ]
