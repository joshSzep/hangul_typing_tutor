from django.urls import path

from hangul_tutor.hangul_tutor_app import views


app_name = "hangul_tutor_app"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
