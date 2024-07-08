from rest_framework import viewsets

from .models import Challenge
from .models import Sentence
from .models import ChallengeResult
from .serializers import ChallengeSerializer
from .serializers import SentenceSerializer
from .serializers import ChallengeResultSerializer


class SentenceViewSet(viewsets.ModelViewSet):
    queryset = Sentence.objects.all()
    serializer_class = SentenceSerializer


class ChallengeViewSet(viewsets.ModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer


class ChallengeResultViewSet(viewsets.ModelViewSet):
    queryset = ChallengeResult.objects.all()
    serializer_class = ChallengeResultSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
