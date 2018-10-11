# Generated by Django 2.1 on 2018-10-11 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_name', models.CharField(max_length=10)),
                ('department', models.CharField(max_length=20)),
                ('post_company', models.CharField(max_length=20)),
                ('release_time', models.DateTimeField()),
                ('expire_time', models.DateTimeField()),
                ('location', models.CharField(max_length=6)),
                ('exp_requirement', models.CharField(max_length=10)),
                ('edu_requirement', models.CharField(max_length=10)),
                ('post_number', models.IntegerField()),
                ('responsibility', models.TextField(max_length=500)),
                ('post_requirement', models.TextField(max_length=500)),
            ],
            options={
                'verbose_name_plural': '岗位管理',
            },
        ),
    ]
