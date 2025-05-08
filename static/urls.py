from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from shop.shop.settings import BASE_DIR
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('mykart.urls')),
]
 
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    STATICFILES_DIRS = [
    BASE_DIR / 'static',]