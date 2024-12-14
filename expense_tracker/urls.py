from django.contrib import admin
from django.urls import path, include  # include is needed for including app URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('expenses.urls')),  # This includes the 'expenses' app URLs
]
