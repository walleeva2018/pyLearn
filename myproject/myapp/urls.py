from django.urls import path
from .views import get_top_categories

urlpatterns = [
    path('top-categories/', get_top_categories, name='top_categories'),
]
