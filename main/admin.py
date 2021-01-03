from django.contrib import admin
from .models import User,Message,Deal,Start


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass

@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    pass

@admin.register(Start)
class StartAdmin(admin.ModelAdmin):
    pass


