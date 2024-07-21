from django.urls import path

from . import views


urlpatterns = [
    path(
        "",
        views.index_page,
        name="index_page",
    ),
    path(
        "tutor/",
        views.tutor_page,
        name="tutor_page",
    ),
    path(
        "start_debug_task/",
        views.start_debug_task,
        name="start_debug_task",
    ),
]
