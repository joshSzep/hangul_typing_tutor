from django.urls import path, include
from rest_framework import routers
from .views import SentenceViewSet, ChallengeViewSet, ChallengeResultViewSet

router = routers.DefaultRouter()
router.register(r'sentences', SentenceViewSet)
router.register(r'challenges', ChallengeViewSet)
router.register(r'challenge_result', ChallengeResultViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
