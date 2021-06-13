from django.db import models
from django.conf import settings
from hitcount.models import HitCount
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.text import slugify

User = settings.AUTH_USER_MODEL


class NamedMixin(models.Model):
    name = models.CharField(max_length=255, unique=True, null=True)

    class Meta:
        abstract = True
        ordering = ["name"]

    def __str__(self):
        return self.name

    class NonUnique(models.Model):
        name = models.CharField(max_length=255, null=True)

        class Meta:
            abstract = True
            ordering = ["name"]

        def __str__(self):
            return self.name


class TimeStampMixin(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+", null=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class Department(NamedMixin, TimeStampMixin):
    pass


class PublishedPublicationManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=True).filter(is_deleted=False)


class Publication(TimeStampMixin, models.Model):
    class Category(models.TextChoices):
        GENERAL = "General"
        CLOSURES = "Closures"
        VACANCIES = "Vacancies"
        CONSULTATIONS = "Consultations"
        JUDICIAL_SALES = "Judicial Sales"
        NEWSLETTERS = "Newsletters"
        TENDERS = "Tenders"

    category = models.CharField(
        max_length=50, choices=Category.choices, default=Category.GENERAL
    )
    title = models.CharField(max_length=100, null=True)
    slug = models.SlugField(max_length=250, unique=True, null=True)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    body = models.TextField(blank=True)
    featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    hit_count_generic = GenericRelation(
        HitCount,
        object_id_field="object_pk",
        related_query_name="hit_count_generic_relation",
    )
    follow = models.BooleanField(default=False)

    objects = models.Manager()
    published_objects = PublishedPublicationManager()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.subject)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


def attachment_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "attachment/{0}/{1}".format(instance.publication.title, filename)


class Attachment(TimeStampMixin):
    name = models.CharField(max_length=50, default="relating document")
    publication = models.ForeignKey(
        Publication, on_delete=models.CASCADE, related_name="attachments"
    )
    file = models.FileField(upload_to=attachment_directory_path)

    def __str__(self):
        return str(self.publication.title)
