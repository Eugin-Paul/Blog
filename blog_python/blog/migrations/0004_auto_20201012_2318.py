# Generated by Django 3.0.7 on 2020-10-12 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201012_2312'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='time',
            new_name='time_view',
        ),
    ]