from django.contrib import admin
from django.urls import path, include # call app

urlpatterns = [
    path('admin/', admin.site.urls),
]