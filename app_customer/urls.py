from django.urls import path
from . import views

urlpatterns = [
      path('alerts/',views.alerts,name="Customer_Alerts_page"),
      path('alert/',views.alertDetails,name="Customer_Alerts_details_page"),
      path('my_profile/',views.myProfile,name="Customer_My_Profile_page"),
]
