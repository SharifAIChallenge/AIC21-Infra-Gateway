from django.urls import path
from ..upload.views import StoreCodeAPIView, StoreMapAPIView

urlpatterns = [
    path('store-code', StoreCodeAPIView.as_view()),
    path('store-map', StoreMapAPIView.as_view()),
]
