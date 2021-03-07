from django.urls import path
from .views import GameLogAPIView, PlayerLogAPIView

urlpatterns = [
    path('game-log', GameLogAPIView.as_view()),
    path('player-log', PlayerLogAPIView.as_view()),
]
