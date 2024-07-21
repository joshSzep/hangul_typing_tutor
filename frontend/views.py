from django.http import JsonResponse
from django.shortcuts import render

from hangul_tutor.celery import debug_task


def start_debug_task(request):
    debug_task.delay()
    return JsonResponse({"status": "Debug task started"})


def index_page(request):
    return render(
        request,
        "frontend/index.html",
        {},
    )


def tutor_page(request):
    # Send a task to celery
    return render(
        request,
        "frontend/tutor.html",
        {},
    )
