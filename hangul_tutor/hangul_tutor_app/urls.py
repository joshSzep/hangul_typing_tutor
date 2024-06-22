from django.urls import path

from hangul_tutor.hangul_tutor_app import views

urlpatterns = [
    path("", views.index, name="index"),
]
