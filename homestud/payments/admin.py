from django.contrib import admin
from .models import UserTransaction, Subscription, AdCampaigns, CheckoutAmount
from django.contrib.admin import ModelAdmin

import json

from django.contrib import admin
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count
from django.db.models.functions import TruncDay
from django.http import JsonResponse
from django.urls import path
from django.db.models import Sum

admin.site.register(Subscription)
admin.site.register(CheckoutAmount)

@admin.register(AdCampaigns)
class CampaignsAdmin(ModelAdmin):
    list_display = ('media', 'start_date', 'end_date', 'amount')

@admin.register(UserTransaction)
class UserTransactionAdmin(ModelAdmin):
    list_display = ('user', 'channel', 'amount', 'date_paid')

    # rendering chartjs in admin tutor profile > change_list view
    def changelist_view(self, request, extra_context=None):
        # Aggregate new subscribers per day
        chart_data = (
            UserTransaction.objects.annotate(date=TruncDay("date_paid"))
            .values("date")
            .annotate(y=Sum('amount')) # sums total amount for columns with the same dates
            .order_by("-date")
        )

        q = UserTransaction.objects.annotate(date=TruncDay("date_paid")).values('date').annotate(total_amt=Sum('amount')).order_by('-date')

        print(q)
        # Serialize and attach the chart data to the template context
        as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
        extra_context = extra_context or {"chart_data": as_json}

        # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=extra_context)

    def get_urls(self):
        urls = super().get_urls()
        extra_urls = [
            path("chart_data/", self.admin_site.admin_view(self.chart_data_endpoint))
        ]
        # NOTE! Our custom urls have to go before the default urls, because they
        # default ones match anything.
        return extra_urls + urls

    # JSON endpoint for generating chart data that is used for dynamic loading
    # via JS.
    def chart_data_endpoint(self, request):
        chart_data = self.chart_data()
        return JsonResponse(list(chart_data), safe=False)

    def chart_data(self):
        return (
            UserTransaction.objects.annotate(date=TruncDay("date_paid"))
            .values("date")
            .annotate(y=Sum('amount')) # sums total amount for columns with the same dates
            .order_by("-date")
        )