from django.contrib import admin

from .models import Client, ClientAuth, ClientToken

class ClientAuthAdmin(admin.ModelAdmin):
    pass

class ClientAdmin(admin.ModelAdmin):
    pass

class ClientTokenAdmin(admin.ModelAdmin):
    list_display = ('client_id','msg_token','created_at')

admin.site.register(ClientAuth, ClientAuthAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(ClientToken, ClientTokenAdmin)

# Register your models here.
