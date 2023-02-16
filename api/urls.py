from django.urls import path
from rest_framework.routers import DefaultRouter

from api.views import NoteViewSet


router = DefaultRouter()
router.register('notes', NoteViewSet, basename='notes')

urlpatterns = [
    
]

urlpatterns += router.urls
