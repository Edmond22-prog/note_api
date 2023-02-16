from rest_framework import serializers

from api.models import Note


class NoteSerializer(serializers.ModelSerializer):
    created_at = serializers.ReadOnlyField()
    updated_at = serializers.ReadOnlyField()
    
    class Meta:
        model = Note
        fields = '__all__'
