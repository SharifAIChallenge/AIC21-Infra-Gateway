from django.urls import path
from ..upload.views import StoreCodeAPIView, StoreMapAPIView

urlpatterns = [
    path('code', StoreCodeAPIView.as_view()),
    path('map', StoreMapAPIView.as_view()),
]
