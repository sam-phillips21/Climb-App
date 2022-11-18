from django.urls import path
from .views import ClimbDetailView, ClimbsView
urlpatterns = [
    path('', ClimbsView.as_view(), name='climbs'),
    path('<int:pk>/', ClimbDetailView.as_view(), name='climbs')
]