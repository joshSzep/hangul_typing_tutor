from django.contrib.auth.models import User
from django.db import models

from core.models import CoreBaseModel


class Sentence(CoreBaseModel):
    hangul = models.TextField()

    def __str__(self):
        return f"{self.id}: {self.hangul}"


class ChallengeResult(CoreBaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    challenge = models.ForeignKey("Challenge", on_delete=models.CASCADE)
    speed = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.id}: {self.user.username} - {self.challenge.name}"


class Challenge(CoreBaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    sentences = models.ManyToManyField(Sentence)
    time_limit = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.name}"
