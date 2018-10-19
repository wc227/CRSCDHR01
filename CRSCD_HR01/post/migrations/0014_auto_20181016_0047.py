# Generated by Django 2.1 on 2018-10-16 00:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0013_auto_20181015_0657'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_stored', models.BooleanField(default=0)),
                ('post', models.ManyToManyField(to='post.Post')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameField(
            model_name='applyinfo',
            old_name='apply_count',
            new_name='user_applied',
        ),
        migrations.RemoveField(
            model_name='applyinfo',
            name='store_count',
        ),
        migrations.RemoveField(
            model_name='applyinfo',
            name='post',
        ),
        migrations.AddField(
            model_name='applyinfo',
            name='post',
            field=models.ManyToManyField(to='post.Post'),
        ),
        migrations.RemoveField(
            model_name='applyinfo',
            name='user',
        ),
        migrations.AddField(
            model_name='applyinfo',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]