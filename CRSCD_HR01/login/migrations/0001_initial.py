# Generated by Django 2.1 on 2018-08-10 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('user_pwd', models.CharField(max_length=20)),
                ('user_email', models.CharField(max_length=30)),
                ('user_phone', models.CharField(max_length=11)),
            ],
        ),
    ]
