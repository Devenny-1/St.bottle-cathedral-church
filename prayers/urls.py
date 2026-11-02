from django.urls import path
from . import views

app_name = 'prayers'

urlpatterns = [
    path('', views.PrayerRequestListView.as_view(), name='prayer_list'),
    path('submit/', views.PrayerRequestCreateView.as_view(), name='prayer_submit'),
]
