# artists/urls.py
from django.urls import path
from .views import WorkListCreateView, WorkDetailView, ArtistWorkListView, ArtistSearchView
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', obtain_auth_token, name='obtain-token'),
    path('works/', WorkListCreateView.as_view(), name='work-list-create'),
    path('works/<int:pk>/', WorkDetailView.as_view(), name='work-detail'),
    path('works/<str:artist_name>/', ArtistWorkListView.as_view(), name='artist-work-list'),
    path('works/search/', ArtistSearchView.as_view(), name='artist-search'),
]
