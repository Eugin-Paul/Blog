# Generated by Django 3.0.7 on 2020-10-14 08:48

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20201012_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(default='new'),
            preserve_default=False,
        ),
    ]
