# Generated by Django 3.0.7 on 2020-10-14 09:10

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20201014_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='overview',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
