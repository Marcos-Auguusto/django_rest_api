from django.urls import path
from .api_views import BookAPIView

urlpatterns = [
    path('', BookAPIView.as_view()),
]