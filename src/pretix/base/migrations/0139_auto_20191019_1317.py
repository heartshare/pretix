# Generated by Django 2.2.1 on 2019-10-19 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0138_auto_20191017_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='geo_lat',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='geo_lon',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='subevent',
            name='geo_lat',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='subevent',
            name='geo_lon',
            field=models.FloatField(null=True),
        ),
    ]