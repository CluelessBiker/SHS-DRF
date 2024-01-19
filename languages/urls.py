from django.urls import path
from languages import views

urlpatterns = [
    path('languages/', views.LanguageList.as_view()),
    path('languages/<int:pk>', views.LanguageDetail.as_view()),
]