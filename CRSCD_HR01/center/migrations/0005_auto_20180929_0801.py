# Generated by Django 2.1 on 2018-09-29 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0004_auto_20180929_0423'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eduinfo',
            old_name='basic_foreignkey',
            new_name='edu_foreignkey',
        ),
    ]
