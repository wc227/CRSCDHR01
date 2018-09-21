from django.db import models


# Create your models here.
class Post(models.Model):
    class Meta:
        verbose_name_plural = '岗位管理'
    post_name = models.CharField(max_length=10)
    department = models.CharField(max_length=20)
    post_company = models.CharField(max_length=20)
    release_time = models.DateTimeField()
    expire_time = models.DateTimeField()
    location = models.CharField(max_length=6)
    exp_requirement = models.CharField(max_length=10)
    edu_requirement = models.CharField(max_length=10)
    post_number = models.IntegerField()
    responsibility = models.TextField(max_length=500)
    post_requirement = models.TextField(max_length=500)


