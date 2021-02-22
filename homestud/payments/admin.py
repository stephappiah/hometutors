from django.contrib import admin
from .models import UserTransaction, Subscription

admin.site.register(UserTransaction)
admin.site.register(Subscription)
