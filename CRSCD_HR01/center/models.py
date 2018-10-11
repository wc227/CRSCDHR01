from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# 简历基本信息
class BasicInfo(models.Model):
    name = models.CharField("姓名", max_length=10)
    phone = models.CharField("手机号", max_length=11)
    age = models.IntegerField("年龄")
    work_year = models.CharField("工龄", max_length=10)
    party = models.CharField("政治面貌", max_length=20)
    live_location = models.CharField("居住地", max_length=20)
    study_location = models.CharField("生源地", max_length=20)
    identity_id = models.CharField("身份证号", max_length=20)
    gender = models.CharField("性别", max_length=1)
    is_Delete = models.BooleanField(default=False)
    reserved_info01 = models.CharField("备注1", max_length=50, null=True, blank=True)
    reserved_info02 = models.CharField("备注2", max_length=50, null=True, blank=True)
    reserved_info03 = models.CharField("备注3", max_length=50, null=True, blank=True)
    reserved_info04 = models.CharField("备注4", max_length=50, null=True, blank=True)
    reserved_info05 = models.IntegerField("备注5", null=True)

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='basic_info',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name.encode('utf-8')

    class Meta:
        verbose_name_plural = '应聘人员'


# 简历工作信息
class WorkInfo(models.Model):
    company = models.CharField("公司", max_length=50, null=True)
    position = models.CharField("职务", max_length=50, null=True)
    work_stime = models.DateField("开始时间", null=True)
    work_etime = models.DateField("结束时间", null=True)
    work_desc = models.CharField("职责描述", max_length=100, null=True)
    reserved_info06 = models.CharField(max_length=50, null=True, blank=True)
    reserved_info07 = models.CharField(max_length=50, null=True, blank=True)
    reserved_info08 = models.CharField(max_length=50, null=True, blank=True)
    reserved_info09 = models.IntegerField(null=True, blank=True)
    work_foreignkey = models.ForeignKey(BasicInfo, related_name="work_info", on_delete=models.CASCADE)

    def __str__(self):
        return self.company

    class Meta:
        verbose_name_plural = '工作信息'


# 简历教育信息
class EduInfo(models.Model):
    school = models.CharField("学校", max_length=50)
    profession = models.CharField("专业", max_length=50)
    education = models.CharField("学历", max_length=20)
    degree = models.CharField("学位", max_length=20)
    school_stime = models.DateField("入学时间")
    school_etime = models.DateField("毕业时间")
    profession_desc = models.CharField(max_length=200)
    reserved_info10 = models.CharField(max_length=50, null=True, blank=True)
    reserved_info11 = models.CharField(max_length=50, null=True, blank=True)
    reserved_info12 = models.CharField(max_length=50, null=True, blank=True)
    reserved_info13 = models.IntegerField(null=True, blank=True)
    edu_foreignkey = models.ForeignKey(BasicInfo, related_name="edu_info", on_delete=models.CASCADE)

    def __str__(self):
        return self.education

    class Meta:
        verbose_name_plural = '教育信息'


# 简历上传函数
def resume_upload(instance, filename):
    return 'resume/{1}'.format(instance, filename)


# 简历文件
class ResumeFile(models.Model):
    resume_file = models.FileField("简历", upload_to='resume/', null=True, blank=True)
    file_name = models.CharField(max_length=100)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='resume',
        on_delete=models.CASCADE,
    )




