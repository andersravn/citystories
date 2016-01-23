from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import UserEntry, Note, DfiFilm


class UserEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEntry
        fields = ('uuid', 'type', 'user', 'text_content', 'rating', 'lat', 'lng', 'pnt', 'created')


class LimitedUserEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEntry
        fields = ('uuid', 'type', 'rating', 'lat', 'lng', 'created')
        read_only_fields = ('uuid', 'type', 'rating', 'lat', 'lng', 'created')


class UuidUserEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEntry
        fields = ('uuid',)
        read_only_fields = ('uuid',)


class UserVoteSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    value = serializers.IntegerField()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'last_login')


class NoteSerializer(serializers.ModelSerializer):
    place = serializers.StringRelatedField()

    class Meta:
        model = Note
        fields = ('uuid', 'type', 'text_content', 'from_date', 'lat', 'lng', 'place', 'rating')
        read_only_fields = ('uuid', 'type', 'text_content', 'from_date', 'lat', 'lng', 'place', 'rating')


class LimitedNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('uuid', 'type', 'lat', 'lng', 'rating')
        read_only_fields = ('uuid', 'type', 'lat', 'lng', 'rating')


class UuidNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('uuid',)
        read_only_fields = ('uuid',)


class DfiFilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = DfiFilm
        fields = ('uuid', 'type', 'title', 'text_content', 'rating', 'duration', 'embed', 'lat', 'long', 'date')
