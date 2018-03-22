from django.contrib import admin

from test_server.apps.tag.models import Tag

class TagAdmin(admin.ModelAdmin):
    list_display = ('title','tag_id','priority','is_publish','edited_at')

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super(TagAdmin, self).save_model(request, obj, form, change)

admin.site.register(Tag, TagAdmin)
