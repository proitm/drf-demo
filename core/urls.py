from django.urls import path

from .views import (
    IndexView, CalculateDistanceView
)


urlpatterns = [
    path('', IndexView.as_view()),
    path('distance/', CalculateDistanceView.as_view()),
]
