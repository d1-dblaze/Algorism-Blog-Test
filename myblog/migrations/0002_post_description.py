# Generated by Django 3.0.14 on 2021-08-03 22:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(default=django.utils.timezone.now, max_length=400),
        ),
    ]
