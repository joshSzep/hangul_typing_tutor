from django.urls import include
from django.urls import path
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r"challenges", views.ChallengeViewSet)
router.register(r"challenge_groups", views.ChallengeGroupViewSet)

urlpatterns = [
    path("v1/", include(router.urls)),
]
