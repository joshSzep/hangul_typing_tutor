from rest_framework import viewsets

from . import models, serializers


class ChallengeViewSet(viewsets.ModelViewSet):
    queryset = models.Challenge.objects.all()
    serializer_class = serializers.ChallengeSerializer


class ChallengeGroupViewSet(viewsets.ModelViewSet):
    queryset = models.ChallengeGroup.objects.all()
    serializer_class = serializers.ChallengeGroupSerializer
