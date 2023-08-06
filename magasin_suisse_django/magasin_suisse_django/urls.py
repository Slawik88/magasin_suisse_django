from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mainapp.views import index_page_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page_view),
]
# Добавьте этот код, чтобы указать маршрут для статических файлов
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)