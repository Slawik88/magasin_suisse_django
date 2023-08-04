from django.contrib import admin
from django.urls import path

from mainapp.views import index_page_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page_view),
]
