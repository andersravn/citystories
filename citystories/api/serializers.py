from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Entry, Note, TestEntry


class EntrySerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Entry
        fields = ('content', 'user', 'created')

    def validate_content(self, value):
        if ' ' in value:
            raise serializers.ValidationError('That was more than one word!')
        return value


class TestEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = TestEntry
        fields = ('text_content', 'lat', 'long', 'pnt')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'last_login')


class NoteSerializer(serializers.ModelSerializer):
    place = serializers.StringRelatedField()

    class Meta:
        model = Note
        fields = ('text_content', 'from_date', 'lat', 'lng', 'place')
