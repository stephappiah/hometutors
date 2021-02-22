from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('findtutors.urls')), #findtutors urls path
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')), #allauth accounts path
    path('chat/', include('chat.urls')),
    path('pay/', include('payments.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
