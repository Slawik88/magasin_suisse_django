from django.contrib import admin
from django.urls import path

from cartApp import views

urlpatterns = [
    path('admin/', admin.site.urls),

]
