from django.urls import include, path
from rest_framework import routers

from .views import (
    ChallengeResultViewSet,
    ChallengeViewSet,
    SentenceViewSet,
    challenge_view,
)

router = routers.DefaultRouter()
router.register(r"sentences", SentenceViewSet)
router.register(r"challenges", ChallengeViewSet)
router.register(r"challenge_result", ChallengeResultViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("challenges/<str:challenge_id>/", challenge_view, name="challenge"),
]
