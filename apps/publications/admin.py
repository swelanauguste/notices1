from django.contrib import admin

from .models import Publication


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ["title", "is_published", "is_deleted"]
    list_editable = ["is_published", "is_deleted"]
