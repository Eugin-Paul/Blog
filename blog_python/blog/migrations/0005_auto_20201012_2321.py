# Generated by Django 3.0.7 on 2020-10-12 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20201012_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time_view',
            field=models.DateField(null=True),
        ),
    ]