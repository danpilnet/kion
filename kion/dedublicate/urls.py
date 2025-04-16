from django.urls import path
from .views import DedublicateView

urlpatterns = [
    path('', DedublicateView.as_view())
]