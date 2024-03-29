# Generated by Django 2.1 on 2018-09-29 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0003_auto_20180929_0317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workinfo',
            name='company',
            field=models.CharField(max_length=50, null=True, verbose_name='公司'),
        ),
        migrations.AlterField(
            model_name='workinfo',
            name='position',
            field=models.CharField(max_length=50, null=True, verbose_name='职务'),
        ),
        migrations.AlterField(
            model_name='workinfo',
            name='work_desc',
            field=models.CharField(max_length=100, null=True, verbose_name='职责描述'),
        ),
        migrations.AlterField(
            model_name='workinfo',
            name='work_etime',
            field=models.DateField(null=True, verbose_name='结束时间'),
        ),
        migrations.AlterField(
            model_name='workinfo',
            name='work_stime',
            field=models.DateField(null=True, verbose_name='开始时间'),
        ),
    ]
