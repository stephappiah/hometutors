from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('findtutors.urls')), #findtutors urls path
    path('users/', include('users.urls')),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('kdf939djfd_admin_3dkfj/', admin.site.urls),
    path('accounts/', include('allauth.urls')), #allauth accounts path
    path('chat/', include('chat.urls')),
    path('pay/', include('payments.urls')),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
    path('maintenance-mode/', include('maintenance_mode.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# change title of admin page to homestud
admin.site.site_header = 'Homestud Admin'
admin.site.site_title = 'Homestud Admin Portal'
admin.site.index_title = 'Welcome to Homestud Admin Portal'
