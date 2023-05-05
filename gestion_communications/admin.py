from django.contrib import admin
from .models import Message, Announcement

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    pass
 