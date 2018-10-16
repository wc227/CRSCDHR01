# Generated by Django 2.1 on 2018-10-16 01:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0015_auto_20181016_0054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applyinfo',
            name='post',
        ),
        migrations.RemoveField(
            model_name='applyinfo',
            name='user',
        ),
        migrations.AddField(
            model_name='post',
            name='applicants',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='ApplyInfo',
        ),
    ]
