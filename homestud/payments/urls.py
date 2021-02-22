from django.urls import path
from .views import checkout, verify_payment


app_name = 'payment'

urlpatterns = [
    path('', checkout, name="checkout"),
    path('verify-payment/<int:id>', verify_payment, name='verify'),
]