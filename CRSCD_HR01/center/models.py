from django.db import models


# 简历基本信息
class BasicInfo(models.Model):
    class Meta:
        verbose_name_plural = '简历'

    name = models.CharField(max_length=10)
    phone = models.CharField(max_length=11)
    age = models.IntegerField()
    work_year = models.CharField(max_length=10)
    political_status = models.CharField(max_length=20)
    live_location = models.CharField(max_length=20)
    study_location = models.CharField(max_length=20)
    identity_id = models.CharField(max_length=20)
    gender = models.CharField(max_length=1)
    photo = models.ImageField(upload_to='center/photo', null=True, blank=True)
    resume = models.FileField(upload_to='center/resume', null=True, blank=True)
    resume_create_time = models.DateTimeField(auto_now_add=True)
    resume_update_time = models.DateTimeField(auto_now=True)
    is_Delete = models.BooleanField(default=False)
    reserved_info01 = models.CharField(max_length=50, null=True, blank=True)
    reserved_info02 = models.CharField(max_length=50, null=True, blank=True)
    reserved_info03 = models.CharField(max_length=50, null=True, blank=True)
    reserved_info04 = models.CharField(max_length=50, null=True, blank=True)
    reserved_info05 = models.IntegerField(null=True)

    def __str__(self):
        return self.name


# 简历工作信息
class WorkInfo(models.Model):
    class Meta:
        verbose_name_plural = '工作信息'

    company = models.CharField(max_length=50)
    post = models.CharField(max_length=50)
    work_start_time = models.DateField()
    work_end_time = models.DateField()
    post_desc = models.CharField(max_length=100)
    reserved_info06 = models.CharField(max_length=50, null=True, blank=True)
    reserved_info07 = models.CharField(max_length=50, null=True, blank=True)
    reserved_info08 = models.CharField(max_length=50, null=True, blank=True)
    reserved_info09 = models.IntegerField(null=True, blank=True)
    work_foreignkey = models.ForeignKey(BasicInfo, on_delete=models.CASCADE)


# 简历教育信息
class EducationInfo(models.Model):
    class Meta:
        verbose_name_plural = '教育信息'

    school = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    education = models.CharField(max_length=20)
    degree = models.CharField(max_length=20)
    school_start_time = models.DateField()
    school_end_time = models.DateField()
    reserved_info10 = models.CharField(max_length=50, null=True, blank=True)
    reserved_info11 = models.CharField(max_length=50, null=True, blank=True)
    reserved_info12 = models.CharField(max_length=50, null=True, blank=True)
    reserved_info13 = models.IntegerField(null=True, blank=True)
    education_foreignkey = models.ForeignKey(BasicInfo, on_delete=models.CASCADE)


