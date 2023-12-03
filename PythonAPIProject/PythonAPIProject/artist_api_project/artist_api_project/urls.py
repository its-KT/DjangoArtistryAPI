# artist_api_project/urls.py
from django.contrib import admin
from django.urls import path, include

from artists.views import UserDetailsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('artists.urls')),
    path('api/user/<str:username>/', UserDetailsView.as_view(), name='user-details'),
]