# Generated by Django 2.2.5 on 2019-10-18 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0007_auto_20191017_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aspectratings',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
