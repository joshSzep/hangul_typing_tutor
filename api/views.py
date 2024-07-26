from rest_framework import viewsets

from . import models, serializers


class ChallengeViewSet(viewsets.ModelViewSet):
    queryset = models.Challenge.objects.all()
    serializer_class = serializers.ChallengeSerializer


class ChallengeGroupViewSet(viewsets.ModelViewSet):
    queryset = models.ChallengeGroup.objects.all()
    serializer_class = serializers.ChallengeGroupSerializer

class TypingSpeedViewSet(viewsets.ModelViewSet):
    queryset = models.TypingSpeed.objects.all()
    serializer_class = serializers.TypingSpeedSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
