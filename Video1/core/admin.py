from django.contrib import admin
from core.models import Film

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ['name', 'director', 'get_tags']

    def get_tags(self, obj):
        return ", ".join(o for o in obj.tags.names())