from django.db import models

from core import models as core_models


class Challenge(core_models.CoreBaseModel):
    hangul = models.TextField()
    english = models.TextField()


class ChallengeGroup(core_models.CoreBaseModel):
    challenges = models.ManyToManyField(Challenge)
