from django.urls import path
from . import views

urlpatterns = [
    path('',views.products,name="Products_page"),
    path('confirm_product/',views.confirmProduct,name="Product_Confirmation_page"),
]
