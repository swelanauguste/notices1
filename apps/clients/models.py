import uuid

from django.conf import settings
from django.db import models
from django.urls import reverse
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="users", null=True, blank=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def get_full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return f"{self.user.username}"

    def get_absolute_url(self):
        return reverse("clients:profile-detail", kwargs={"uuid": self.uuid})

    def __str__(self):
        return f"{self.user.username}'s profile"

    def save(self, *args, **kwargs):
        super().save()
        if self.photo:
            img = Image.open(self.photo.path)

        # When image height is greater than its width
        if self.photo:
            if img.height > img.width:
                # make square by cutting off equal amounts top and bottom
                left = 0
                right = img.width
                top = (img.height - img.width) / 2
                bottom = (img.height + img.width) / 2
                img = img.crop((left, top, right, bottom))
                # Resize the image to 300x300 resolution
                if img.height > 300 or img.width > 300:
                    output_size = (300, 300)
                    img.thumbnail(output_size)
                    img.save(self.photo.path)

            # When image width is greater than its height

            elif img.width > img.height:
                # make square by cutting off equal amounts left and right
                left = (img.width - img.height) / 2
                right = (img.width + img.height) / 2
                top = 0
                bottom = img.height
                img = img.crop((left, top, right, bottom))
                # Resize the image to 300x300 resolution
                if img.height > 300 or img.width > 300:
                    output_size = (300, 300)
                    img.thumbnail(output_size)
                    img.save(self.photo.path)
