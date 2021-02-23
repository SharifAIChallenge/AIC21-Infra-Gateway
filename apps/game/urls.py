from django.urls import path
from .views import PlayGameAPIView

urlpatterns = [
    path('play', PlayGameAPIView.as_view()),
]
