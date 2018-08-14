from django.db import models


# Create your models here.
class UserInfo(models.Model):
    user_pwd = models.CharField(max_length=50)
    user_email = models.CharField(max_length=30)
    user_phone = models.CharField(max_length=11)


