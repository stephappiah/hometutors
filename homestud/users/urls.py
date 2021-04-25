from django.urls import path
from django.conf.urls import url
from .views import homestud_email

app_name = 'users'

urlpatterns = [
    path('email-users/', homestud_email, name="email-users"),
]