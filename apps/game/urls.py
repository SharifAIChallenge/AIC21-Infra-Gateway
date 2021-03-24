from django.urls import path
from .views import PlayGameAPIView

urlpatterns = [
    path('register', PlayGameAPIView.as_view()),
]
