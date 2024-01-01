from django.urls import path
from practitioners import views

urlpatterns = [
    path('practitioners/', views.PractitionerList.as_view()),
    path('practitioners/<int:pk>', views.PractitionerDetail.as_view()),
]