from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework import viewsets

from api.models import Note
from api.serializers import NoteSerializer


class NoteViewSet(
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    viewsets.GenericViewSet):
    
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
