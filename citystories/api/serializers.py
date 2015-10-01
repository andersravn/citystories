from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Note, UserEntry


class UserEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEntry
        fields = ('id', 'text_content', 'rating', 'lat', 'lng', 'pnt', 'created')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'last_login')


class NoteSerializer(serializers.ModelSerializer):
    place = serializers.StringRelatedField()

    class Meta:
        model = Note
        fields = ('id', 'text_content', 'from_date', 'lat', 'lng', 'place', 'rating')
