import re

from django.db import models
from uuid_extensions import uuid7str


class CoreBaseModel(models.Model):
    id = models.CharField(
        max_length=64,  # 36 characters for UUID + 28 reserved for prefix
        primary_key=True,
        editable=False,
        unique=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True, default=None)

    class Meta:
        abstract = True

    @classmethod
    def get_prefix(cls):
        name = re.sub(r"(?<!^)(?=[A-Z])", "_", cls.__name__).lower()
        return name[:28]

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = f"{self.get_prefix()}:{uuid7str()}"
        super().save(*args, **kwargs)
