# -*- coding: utf-8 -*-

from django.db import models



class Message(models.Model):

    ACTIONS_CHOICES = (
        ('oa','打开APP'),
        ('op', '打开指定页面'),
    )

    SCOPE_CHOICES = (
        ('all', 'All'),
        ('android', 'Android'),
        ('ios', 'iOS'),
    )

    TIME_CHOICES = (
        ('immediate','立即推送'),
        ('timing', '定时推送'),
    )

    title = models.CharField(max_length=25, verbose_name="标题")
    content = models.TextField(max_length=250, verbose_name="内容")
    actions = models.CharField(max_length=2, choices=ACTIONS_CHOICES, default='打开APP', verbose_name="点击通知操作")
    scope = models.CharField(max_length=7, choices=SCOPE_CHOICES, default='All', verbose_name="用户范围")
    time = models.CharField(max_length=10, choices=TIME_CHOICES , default='立即推送', verbose_name="推送时间")
    # icon = models.ImageField(upload_to='icon',width_field=45,height_field=45, verbose_name="图标")
    available = models.BooleanField(default=False, verbose_name="是否可用")

    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)



    class Meta:
        db_table="message"
        get_latest_by = 'edited_at'
        verbose_name_plural = '消息推送管理'
        verbose_name = '消息推送管理'

    def __str__(self):
        return self.title

