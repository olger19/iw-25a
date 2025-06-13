from django.urls import path
from .views import newsView

urlpatterns = [
    path('', newsView, name='home'),
]
