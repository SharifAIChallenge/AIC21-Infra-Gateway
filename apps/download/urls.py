from django.urls import path
from .views import GameLogAPIView, CodeAPIView

urlpatterns = [
    path('log', GameLogAPIView.as_view()),
    path('code', CodeAPIView.as_view()),
]
