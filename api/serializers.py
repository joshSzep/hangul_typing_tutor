from rest_framework import serializers

from . import models


class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Challenge
        fields = "__all__"


class ChallengeGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ChallengeGroup
        fields = "__all__"
