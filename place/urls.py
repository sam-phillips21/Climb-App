from django.urls import path
from .views import LocationDetailView, LocationsView
urlpatterns = [
    path('', LocationsView.as_view(), name='locations'),
    path('<int:pk>/', LocationDetailView.as_view(), name='locations')
]