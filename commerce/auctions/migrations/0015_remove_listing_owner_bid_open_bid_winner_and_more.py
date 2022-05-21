# Generated by Django 4.0.4 on 2022-05-21 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_bid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='owner',
        ),
        migrations.AddField(
            model_name='bid',
            name='open',
            field=models.BooleanField(default='True'),
        ),
        migrations.AddField(
            model_name='bid',
            name='winner',
            field=models.TextField(blank=True, max_length=400),
        ),
        migrations.AddField(
            model_name='listing',
            name='winning_bid',
            field=models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.bid'),
            preserve_default=False,
        ),
    ]