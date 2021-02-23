from django.urls import path
from ..upload.views import StoreCodeAPIView


urlpatterns = [
    path('store-code', StoreCodeAPIView.as_view()),
]
