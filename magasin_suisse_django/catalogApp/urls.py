from django.urls import path

from . import views
from .views import index_page_view
from django.urls import path, include

from . import views
from .views import index_page_view

urlpatterns = [
    path('category/subcategories/<slug:category_slug>/', views.get_subcategories, name='get_subcategories'),
]
