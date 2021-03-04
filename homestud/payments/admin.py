from django.contrib import admin
from .models import UserTransaction, Subscription, AdCampaigns
from django.contrib.admin import ModelAdmin

admin.site.register(UserTransaction)
admin.site.register(Subscription)

@admin.register(AdCampaigns)
class CampaignsAdmin(ModelAdmin):
    list_display = ('media', 'start_date', 'end_date', 'amount')
