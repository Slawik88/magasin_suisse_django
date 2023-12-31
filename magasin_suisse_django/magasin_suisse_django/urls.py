from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from catalogApp.views import index_page_view
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page_view, name='home'),
    path('category/', include('catalogApp.urls')),
    path('cart/', include('cartApp.urls')),
    path('user/', include('usersApp.urls')),
    path('payment-and-orders/', include('payment_and_orders_App.urls'))

]
# Добавьте этот код, чтобы указать маршрут для статических файлов
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
