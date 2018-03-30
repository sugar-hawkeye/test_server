from django.contrib import admin

from .models import Message

class MessageAdmin(admin.ModelAdmin):

    radio_fields = {"actions": admin.HORIZONTAL,"scope": admin.HORIZONTAL,"time": admin.HORIZONTAL}

admin.site.register(Message, MessageAdmin)


admin.AdminSite.site_header = '测试组件管理'
admin.AdminSite.site_title = '测试组件管理'
admin.AdminSite.index_title = '测试组件管理'