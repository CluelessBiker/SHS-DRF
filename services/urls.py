from django.urls import path
from services import views

urlpatterns = [
    path('services/', views.ServiceList.as_view()),
    path('services/<int:pk>/', views.ServiceDetail.as_view()),
]