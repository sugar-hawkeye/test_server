from django.db import models


from django.contrib.auth.models import User

# Create your models here.
from test_server.apps.tag.models import Tag


class Video(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, editable=False, on_delete=models.SET_NULL, verbose_name="创建人", null=True,
                                   blank=True)

    video_name = models.CharField(max_length=50, verbose_name="视频标题")
    video_desc = models.TextField(verbose_name="视频描述")
    publish_time = models.DateField(verbose_name="上映时间", null=True, blank=True)
    is_serial = models.BooleanField(default=False, verbose_name="是否是剧集")
    tag_id = models.ManyToManyField(
        Tag,
        verbose_name='标签',
    )

    class Meta:
        db_table="video"
        get_latest_by = 'created_at'
        ordering = ['created_at']
        verbose_name = '视频'
        verbose_name_plural = '视频'

    def __str__(self):
        return self.video_name

# class VideoList(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     edited_at = models.DateTimeField(auto_now=True)
#     created_by = models.ForeignKey(User, editable=False, on_delete=models.SET_NULL, verbose_name="创建人",null=True,blank=True)
#
#     video_id = models.ForeignKey(Video,on_delete=models.CASCADE,verbose_name='视频id')
#     video_name = models.CharField(max_length=50,verbose_name="视频名")
#     video_index = models.IntegerField(verbose_name="剧集数",default=0,help_text="如果是剧集则按集数填写")
#     video_url = models.URLField(verbose_name="视频地址")
#     video_icon = models.ImageField(upload_to=UploadUtils.video_path,verbose_name="封面")
#     desc = models.CharField(max_length=8,null=True,blank=True,help_text="如果是剧集则必须填写",verbose_name="视频描述")
#     is_publish = models.BooleanField(default=False, verbose_name="是否发布")
#
#     class Meta:
#         db_table="video_list"
#         get_latest_by = 'created_at'
#         ordering = ['created_at']
#         verbose_name = '视频列表'
#         verbose_name_plural = '视频列表'
#
#     def __unicode__(self):
#         return self.video_id.video_name