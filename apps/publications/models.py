from django.db import models
from django.conf import settings
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation

User = settings.AUTH_USER_MODEL


class PublishedPublicationManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=True).filter(is_deleted=False)


class Publication(models.Model):
    class Category(models.TextChoices):
        CLOSURES = "CS", "Closures"
        VACANCIES = "VS", "Vacancies"

    category = models.CharField(
        max_length=50, choices=Category.choices, default=Category.CLOSURES
    )
    title = models.CharField(max_length=100, null=True)
    is_published = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    hit_count_generic = GenericRelation(
        HitCount,
        object_id_field="object_pk",
        related_query_name="hit_count_generic_relation",
    )

    objects = models.Manager()
    published_objects = PublishedPublicationManager()

    def __str__(self):
        return self.title

