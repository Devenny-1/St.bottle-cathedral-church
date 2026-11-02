from django.urls import path
from . import views

app_name = 'donations'

urlpatterns = [
    path('', views.DonationView.as_view(), name='donate'),
    path('success/', views.DonationSuccessView.as_view(), name='donation_success'),
]
