from django.urls import path, include
from .views import SearchAPIView


urlpatterns = [
    path('bus/', SearchAPIView.as_view()),
]
