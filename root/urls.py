from django.contrib import admin
from django.urls import path

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),
]
