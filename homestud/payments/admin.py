from django.contrib import admin
from .models import UserTransaction, Subscription, AdCampaigns, CheckoutAmount
from django.contrib.admin import ModelAdmin

admin.site.register(UserTransaction)
admin.site.register(Subscription)
admin.site.register(CheckoutAmount)

@admin.register(AdCampaigns)
class CampaignsAdmin(ModelAdmin):
    list_display = ('media', 'start_date', 'end_date', 'amount')
