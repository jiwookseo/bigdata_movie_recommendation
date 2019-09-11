from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFit


def image_path(instance, filename):
    return 'profile/{}/{}'.format(instance.id, filename)


class User(AbstractUser):
    gender = models.CharField(max_length=10, default='M')
    age = models.IntegerField(default=25)
    occupation = models.CharField(max_length=200)
    cluster = models.IntegerField(default=-1)
    refresh_token = models.TextField(default="")
    image = ProcessedImageField(
        upload_to=image_path,
        processors=[ResizeToFit(width=150, upscale=False)],
        format='JPEG',
        blank=True
    )
    thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFit(width=50, upscale=False)],
        format='JPEG',
        options={'quality': 60}
    )

    def __str__(self):
        return "{}".format(self.username)

    @property
    def rating_cnt(self):
        return len(self.ratings.all())
