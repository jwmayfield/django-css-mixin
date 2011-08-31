from django.db import models


class CSSMixin(models.Model):
    attr_id = models.CharField(max_length=255, blank=True)
    attr_class = models.CharField(max_length=255, blank=True)
    attr_style = models.TextField(blank=True)

    class Meta:
        abstract = True
