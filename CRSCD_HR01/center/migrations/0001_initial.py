# Generated by Django 2.1 on 2018-09-28 02:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='姓名')),
                ('phone', models.CharField(max_length=11, verbose_name='手机号')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('work_year', models.CharField(max_length=10, verbose_name='工龄')),
                ('party', models.CharField(max_length=20, verbose_name='政治面貌')),
                ('live_location', models.CharField(max_length=20, verbose_name='居住地')),
                ('study_location', models.CharField(max_length=20, verbose_name='生源地')),
                ('identity_id', models.CharField(max_length=20, verbose_name='身份证号')),
                ('gender', models.CharField(max_length=1, verbose_name='性别')),
                ('resume', models.FileField(blank=True, null=True, upload_to='center/resume', verbose_name='简历')),
                ('resume_create_time', models.DateTimeField(auto_now_add=True, verbose_name='')),
                ('resume_update_time', models.DateTimeField(auto_now=True, verbose_name='')),
                ('is_Delete', models.BooleanField(default=False)),
                ('reserved_info01', models.CharField(blank=True, max_length=50, null=True)),
                ('reserved_info02', models.CharField(blank=True, max_length=50, null=True)),
                ('reserved_info03', models.CharField(blank=True, max_length=50, null=True)),
                ('reserved_info04', models.CharField(blank=True, max_length=50, null=True)),
                ('reserved_info05', models.IntegerField(null=True)),
                ('user', models.OneToOneField(default=99, on_delete=django.db.models.deletion.CASCADE, related_name='基本信息', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '应聘人员',
            },
        ),
        migrations.CreateModel(
            name='EduInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=50, verbose_name='学校')),
                ('profession', models.CharField(max_length=50, verbose_name='专业')),
                ('education', models.CharField(max_length=20, verbose_name='学历')),
                ('degree', models.CharField(max_length=20, verbose_name='学位')),
                ('school_stime', models.DateField(verbose_name='入学时间')),
                ('school_etime', models.DateField(verbose_name='毕业时间')),
                ('profession_desc', models.CharField(max_length=200)),
                ('reserved_info10', models.CharField(blank=True, max_length=50, null=True)),
                ('reserved_info11', models.CharField(blank=True, max_length=50, null=True)),
                ('reserved_info12', models.CharField(blank=True, max_length=50, null=True)),
                ('reserved_info13', models.IntegerField(blank=True, null=True)),
                ('basic_foreignkey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='教育信息', to='center.BasicInfo')),
            ],
            options={
                'verbose_name_plural': '教育信息',
            },
        ),
        migrations.CreateModel(
            name='WorkInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=50, verbose_name='公司')),
                ('position', models.CharField(max_length=50, verbose_name='职务')),
                ('work_stime', models.DateField(verbose_name='开始时间')),
                ('work_etime', models.DateField(verbose_name='结束时间')),
                ('work_desc', models.CharField(max_length=100, verbose_name='职责描述')),
                ('reserved_info06', models.CharField(blank=True, max_length=50, null=True)),
                ('reserved_info07', models.CharField(blank=True, max_length=50, null=True)),
                ('reserved_info08', models.CharField(blank=True, max_length=50, null=True)),
                ('reserved_info09', models.IntegerField(blank=True, null=True)),
                ('work_foreignkey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='工作信息', to='center.BasicInfo')),
            ],
            options={
                'verbose_name_plural': '工作信息',
            },
        ),
    ]
