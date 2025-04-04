# Generated by Django 3.2.5 on 2023-08-05 13:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cover_image',
            field=models.ImageField(default=datetime.datetime(2023, 8, 5, 13, 27, 29, 54422, tzinfo=utc), upload_to='post_covers/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='html_file',
            field=models.FileField(default=datetime.datetime(2023, 8, 5, 13, 27, 54, 393702, tzinfo=utc), upload_to='post_html/'),
            preserve_default=False,
        ),
    ]
