from rest_framework import serializers

from .models import Challenge
from .models import ChallengeResult
from .models import Sentence


class SentenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sentence
        fields = "__all__"


class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = "__all__"


class ChallengeResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChallengeResult
        fields = "__all__"
