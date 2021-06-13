from django.contrib import admin

from .models import Publication, Department, Attachment


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ["title", "is_published", "is_deleted"]
    list_editable = ["is_published", "is_deleted"]
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Department)


@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ("name", "publication", "created_at")
