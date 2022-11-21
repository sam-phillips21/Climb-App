from django.urls import path
from .views.climb_views import ClimbDetailView, ClimbsView
from .views.comment_views import Comments, CommentDetail
urlpatterns = [
    path('', ClimbsView.as_view(), name='climbs'),
    path('<int:pk>/', ClimbDetailView.as_view(), name='climbs'),
    path('', Comments.as_view(), name='comments'),
    path('<int:pk>/', CommentDetail.as_view(), name='comments'),
]