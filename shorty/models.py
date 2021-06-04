from django.db import models

from shorty.manager import UrlManager


class Url(models.Model):
    long_url = models.URLField()
    short_id = models.SlugField()
    counter = models.IntegerField(default=0)

    def __str__(self):
        return "%s -- %s" % (self.long_url, self.short_id)

    objects = UrlManager()