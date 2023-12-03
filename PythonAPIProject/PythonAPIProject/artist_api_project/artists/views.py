# artists/views.py
from rest_framework import generics, permissions
from .models import Artist, Work
from .serializers import ArtistSerializer, WorkSerializer


from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            # Additional logic after successful registration, if needed
            pass
        return response

class UserDetailsView(APIView):
    def get(self, request, username, format=None):
        user = User.objects.filter(username=username).first()
        if user:
            data = {
                "username": user.username,
                "email": user.email,
                # Add other fields you want to include
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

class WorkListCreateView(generics.ListCreateAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class WorkDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        work_type = self.request.query_params.get('work_type')
        return Work.objects.filter(work_type=work_type)

class ArtistWorkListView(generics.ListAPIView):
    serializer_class = WorkSerializer

    def get_queryset(self):
        work_type = self.request.query_params.get('work_type')
        queryset = Work.objects.filter(work_type__iexact=work_type) if work_type else Work.objects.all()
        return queryset

class ArtistSearchView(generics.ListAPIView):
    serializer_class = ArtistSerializer

    def get_queryset(self):
        artist_name = self.request.query_params.get('artist')
        return Artist.objects.filter(name__icontains=artist_name)
