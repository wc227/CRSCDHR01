# Generated by Django 2.1 on 2018-10-17 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0017_auto_20181016_0144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='applicants',
        ),
        migrations.RemoveField(
            model_name='post',
            name='favorites',
        ),
        migrations.AlterField(
            model_name='post',
            name='is_delete',
            field=models.BooleanField(default=0, verbose_name='是否删除'),
        ),
    ]
