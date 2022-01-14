from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('webpush/', include('webpush.urls')),
    path('', include('app_accounts.urls')),
    path('super_admin/', include('app_admin.urls')),
    path('ecc/', include('app_ecc.urls')),
    path('customer/', include('app_customer.urls')),
    path('products/', include('app_products.urls')),
]
