# artists/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Artist, Work

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ('link', 'work_type')

class ArtistSerializer(serializers.ModelSerializer):
    works = WorkSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ('name', 'works')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
