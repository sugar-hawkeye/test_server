# -*- coding: utf-8 -*-

from django.db import models

from django.contrib.auth.models import User
from test_server.apps.uidgenerator.models import UIDField

class Tag(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    # created_by = models.ForeignKey(User, editable=False, on_delete=models.SET_NULL, verbose_name="创建人", null=True,
    #                                blank=True)

    owner = models.ForeignKey(User,related_name='tags',on_delete=models.CASCADE,null=True,blank=True)


    tag_id = UIDField(primary_key=True,blank=True)
    title = models.CharField(max_length=15, verbose_name='标签名', unique=True)
    priority = models.IntegerField(verbose_name="排列顺序", blank=True, null=True)
    is_publish = models.BooleanField(default=False, verbose_name="是否发布")
    #code = models.CharField(max_length=100,null=False,editable=False,blank=True)

    class Meta:
        db_table="tag"
        get_latest_by = 'created_at'
        ordering = ['created_at']
        verbose_name = '标签'
        verbose_name_plural = '标签'
        # permissions = (
        #     ("tag_publish", "Can Publish Tag"),
        #     ("tag_delete", "Can Delete Tag"),
        # )



    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save(force_insert,force_update,using,update_fields)

    def __str__(self):
        return self.title