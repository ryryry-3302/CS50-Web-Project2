# Generated by Django 4.0.4 on 2022-05-02 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('desc', models.CharField(max_length=400)),
                ('start_bid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('imgurl', models.CharField(blank=True, max_length=200)),
                ('catego', models.CharField(blank=True, choices=[('HO', 'Home'), ('EL', 'Electronics'), ('SO', 'Sports'), ('TO', 'Toys'), ('FA', 'Fashion')], max_length=2)),
            ],
        ),
    ]