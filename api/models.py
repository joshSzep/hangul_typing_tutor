from django.db import models

from core import models as core_models
from django.contrib.auth.models import User


class Challenge(core_models.CoreBaseModel):
    hangul = models.TextField()
    english = models.TextField()


class ChallengeGroup(core_models.CoreBaseModel):
    challenges = models.ManyToManyField(Challenge)

class TypingSpeed(core_models.CoreBaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    speed = models.IntegerField()  # Speed in symbols per minute
    accuracy = models.FloatField()  # Accuracy as a percentage

    class Meta:
        ordering = ['-created_at']
