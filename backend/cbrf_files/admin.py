from django.contrib import admin
from cbrf_files.models import CBRF_Deposit


class CBRFDepositAdmin(admin.ModelAdmin):
    list_display = ['uploaded_date', 'photo']

    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        CBRF_Deposit.objects.all().delete()
        instance.save()
        return instance

admin.site.register(CBRF_Deposit, CBRFDepositAdmin)
