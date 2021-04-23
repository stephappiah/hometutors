from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import TutorProfile, TutorReview, UserProfile
# from django.contrib.auth.admin import UserAdmin
# from .models import User

import json

from django.contrib import admin
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count
from django.db.models.functions import TruncDay
from django.http import JsonResponse
from django.urls import path
from django.utils.safestring import mark_safe 


# admin.site.register(User, UserAdmin)
admin.site.register(TutorReview)

admin.site.register(UserProfile)

@admin.register(TutorProfile) 
class ProfileAdmin(OSMGeoAdmin):
    list_display = ('user', 'first_name', 'address', 'highest_education', 'slug', 'admin_show', 'show_profile')

    # display avatar image
    readonly_fields = ["headshot_image"]

    def headshot_image(self, obj):
        return mark_safe('<img src="{url}" width="160px" height="160px" style="{style}">'.format(
            url = obj.avatar.url,
            width=obj.avatar.width,
            height=obj.avatar.height,
            style="border-radius: 50%; object-fit: cover;"
            )
    )

    # rendering chartjs in admin tutor profile > change_list view
    def changelist_view(self, request, extra_context=None):
        # Aggregate new subscribers per day
        chart_data = (
            TutorProfile.objects.annotate(date=TruncDay("created_at"))
            .values("date")
            .annotate(y=Count("id"))
            .order_by("-date")
        )

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
            TutorProfile.objects.annotate(date=TruncDay("created_at"))
            .values("date")
            .annotate(y=Count("id"))
            .order_by("-date")
        )