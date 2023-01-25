# Generated by Django 4.1.4 on 2023-01-04 12:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_bids_bid_price_commments'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='watchList',
            field=models.ManyToManyField(blank=True, null=True, related_name='watch', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='commments',
            name='content',
            field=models.CharField(max_length=256),
        ),
    ]