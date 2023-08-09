from django.urls import path

from . import views
from .views import index_page_view, product_details_page
from django.urls import path, include

from . import views
from .views import index_page_view

urlpatterns = [
    path('category/subcategories/<slug:category_slug>/', views.get_categoris_and_subcategories_and_product, name='get_subcategories'),
    path('product/details/<slug:product_slug>', views.product_details_page, name='product_details')
]
