from django.urls import path
from locations import views

urlpatterns = [
    path('locations/', views.LocationList.as_view(),
]