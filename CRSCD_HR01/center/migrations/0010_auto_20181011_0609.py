# Generated by Django 2.1 on 2018-10-11 06:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0009_auto_20181011_0258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumefile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='resume', to=settings.AUTH_USER_MODEL),
        ),
    ]
