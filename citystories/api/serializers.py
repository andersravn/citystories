from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import UserEntry, Note, DfiFilm, Feedback


class UserEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEntry
        fields = ('uuid', 'type', 'user', 'text_content', 'rating', 'lat', 'lng', 'pnt', 'created')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'last_login')


class NoteSerializer(serializers.ModelSerializer):
    place = serializers.StringRelatedField()
    userentries = UserEntrySerializer(many=True, read_only=True)

    class Meta:
        model = Note
        fields = ('uuid', 'type', 'text_content', 'from_date', 'lat', 'lng', 'place', 'rating', 'userentries')


class DfiFilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = DfiFilm
        fields = ('uuid', 'type', 'title', 'text_content', 'rating', 'duration', 'embed', 'lat', 'long', 'date')


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('text_content', 'email')
