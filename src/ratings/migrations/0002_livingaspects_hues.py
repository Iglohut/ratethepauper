# Generated by Django 2.2.5 on 2019-10-13 08:03

from django.db import migrations
import ratings.models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='livingaspects',
            name='hues',
            field=ratings.models.ListField(blank=True, null=True, token=','),
        ),
    ]
