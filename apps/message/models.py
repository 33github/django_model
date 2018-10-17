from __future__ import unicode_literals

#_*_ coding:utf-8 _*_
from django.db import models

# Create your models here.

class UserMessage(models.Model):
    object_id = models.CharField(max_length=50,primary_key=True,verbose_name=u"主键")
    name = models.CharField(max_length=20,verbose_name=u"用户名")
    email = models.EmailField(verbose_name=u"邮箱")
    address = models.CharField(max_length=100,verbose_name=u"联系地址")
    message = models.CharField(max_length=100,verbose_name=u"留言信息")

    class Mata:
        verbose_name = u"用户留言信息"   #你的模型类起一个更可读的名字一般定义为中文
        verbose_name_plural = verbose_name   #指定模型的复数形式,如果不指定Django会自动在模型名称后加一个’s’
        # db_table = "user_message"   #指定自定义数据库表名
        # ordering = "-object_id"   #按照object_id倒序排列

