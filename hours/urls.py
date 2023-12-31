from django.urls import path
from hours import views

urlpatterns = [
    path('hours/', views.HourList.as_view()),
    path('hours/<int:pk>', views.HourDetail.as_view()),
]