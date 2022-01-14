from django.urls import path
from . import views

urlpatterns = [
      path('alerts/',views.alerts,name="ECC_Alerts_page"),
      path('alert/',views.alertDetails,name="ECC_Alerts_details_page"),
      path('my_profile/',views.myProfile,name="ECC_My_Profile_page"),
]
