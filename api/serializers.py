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

class TypingSpeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TypingSpeed
        fields = ['id', 'user', 'challenge', 'speed', 'accuracy', 'created_at']
