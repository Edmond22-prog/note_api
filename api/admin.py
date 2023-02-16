from django.contrib import admin

from api.models import Note


@admin.site.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at', 'updated_at')
