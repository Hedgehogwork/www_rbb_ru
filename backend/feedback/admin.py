from django.contrib import admin
from feedback.models import Theme, Receiver, Feedback


class ThemeAdmin(admin.ModelAdmin):
    pass

class ReceiverAdmin(admin.ModelAdmin):
    pass

class FeedbackAdmin(admin.ModelAdmin):
    pass


admin.site.register(Theme, ThemeAdmin)
admin.site.register(Receiver, ReceiverAdmin)
admin.site.register(Feedback, FeedbackAdmin)
