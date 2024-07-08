import re

from django.db import models
from uuid_extensions import uuid7str


class CoreBaseModel(models.Model):
    id = models.CharField(
        max_length=42,  # 36 characters for UUID + 5 characters for prefix + 1 just cuz
        primary_key=True,
        editable=False,
        unique=True,
    )
    active = models.BooleanField(default=True)  # Soft delete field
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    @classmethod
    def get_prefix(cls):
        name = re.sub(r"(?<!^)(?=[A-Z])", "_", cls.__name__).lower()
        return name[:4]

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = f"{self.get_prefix()}_{uuid7str()}"
        super().save(*args, **kwargs)
