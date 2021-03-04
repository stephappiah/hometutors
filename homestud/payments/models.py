from django.db import models
from django.conf import settings


class UserTransaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='transaction')
    reference = models.CharField(max_length=50, blank=True, null=True)
    channel = models.CharField(max_length=50, blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
       return self.user.email

class Subscription (models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='subscription', on_delete=models.CASCADE)
    start_date = models.DateField(null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)

    def __str__(self):
       return self.user.email


media_list = (
        ('Facebook/Instagram', 'Facebook/Instagram'),
        ('Twitter', 'Twitter'),
        ('SEO', 'SEO'),
        ('Google Adsense', 'Google Adsense'),
        ('Banner', 'Banner'),
)

class AdCampaigns(models.Model):
    media = models.CharField(max_length=20, choices=media_list, null=True, blank=False)
    start_date = models.DateField()
    end_date = models.DateField()
    amount = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.media