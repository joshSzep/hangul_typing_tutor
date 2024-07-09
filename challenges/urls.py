from django.urls import include
from django.urls import path
from rest_framework import routers

from .views import ChallengeResultViewSet
from .views import ChallengeViewSet
from .views import SentenceViewSet
from .views import challenge_view


router = routers.DefaultRouter()
router.register(r"sentences", SentenceViewSet)
router.register(r"challenges", ChallengeViewSet)
router.register(r"challenge_results", ChallengeResultViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("challenges/<str:challenge_id>/", challenge_view, name="challenge"),
]
