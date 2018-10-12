# Generated by Django 2.1 on 2018-10-12 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_auto_20181012_0643'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='apply_type',
            field=models.CharField(choices=[('校园招聘', '校园招聘'), ('社会招聘', '社会招聘')], default='社会招聘', max_length=10, verbose_name='招聘类型'),
        ),
        migrations.AddField(
            model_name='post',
            name='location',
            field=models.CharField(choices=[('北京', '北京'), ('上海', '上海'), ('成都', '成都'), ('沈阳', '沈阳'), ('广州', '广州'), ('武汉', '武汉'), ('西安', '西安'), ('新疆', '新疆'), ('济南', '济南'), ('昆明', '昆明'), ('兰州', '兰州'), ('南昌', '南昌'), ('南宁', '南宁'), ('郑州', '郑州')], default='北京', max_length=10, verbose_name='工作地'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.CharField(choices=[('科研开发', '科研开发'), ('设计专业', '设计专业'), ('系统集成', '系统集成'), ('测试专业', '测试专业'), ('市场经营', '市场经营'), ('生产售后', '生产售后'), ('综合管理', '综合管理'), ('人力资源', '人力资源'), ('财务', '财务'), ('采购', '采购'), ('法律合规', '法律合规'), ('科学研究', '科学研究'), ('战略规划', '战略规划'), ('博士后', '博士后'), ('海外市场', '海外市场'), ('项目管理', '项目管理')], default='综合管理', max_length=10, verbose_name='岗位类型'),
        ),
    ]
