from django.urls import path
from . import views

urlpatterns = [
      path('alerts/',views.alerts,name="Admin_Alerts_page"),
      path('alert/',views.alertDetails,name="Admin_Alerts_details_page"),
      path('eccs/',views.eccList,name="Admin_ECC_list_page"),
      path('ecc/',views.eccProfile,name="Admin_ECC_details_page"),
      path('add_ecc/',views.eccAdd,name="Admin_Add_ECC_page"),
      path('customers/',views.customerList,name="Admin_Customer_list_page"),
      path('customer/',views.customerProfile,name="Admin_Customer_details_page"),
]
