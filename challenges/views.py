from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework import viewsets

from .models import Challenge
from .models import ChallengeResult
from .models import Sentence
from .serializers import ChallengeResultSerializer
from .serializers import ChallengeSerializer
from .serializers import SentenceSerializer


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


def challenge_view(request, challenge_id):
    challenge = get_object_or_404(Challenge, pk=challenge_id)
    sentence = challenge.sentences.order_by("?").first()  # Get a random sentence
    context = {
        "challenge": challenge,
        "sentence": sentence,
    }
    return render(request,"challenges/challenge.html", context)
