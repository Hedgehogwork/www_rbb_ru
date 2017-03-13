from django.contrib import admin
from models import Theme, Receiver, Feedback


class ThemeAdmin(admin.ModelAdmin):
    list_display = ['name']


class ReceiverAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


class FeedbackAdmin(admin.ModelAdmin):
    pass


admin.site.register(Theme, ThemeAdmin)
admin.site.register(Receiver, ReceiverAdmin)
admin.site.register(Feedback, FeedbackAdmin)
