# Generated by Django 4.2.1 on 2023-08-17 11:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_posts_likesdislikes_follower'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='timestamp',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2023, 8, 17, 16, 54, 16, 251876)),
        ),
    ]
