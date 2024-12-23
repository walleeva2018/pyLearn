from django.urls import path
from .views import signature_verification

urlpatterns = [
    path('verify/', signature_verification, name='signature_verification'),
]
