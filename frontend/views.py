from django.shortcuts import render


def index_page(request):
    return render(
        request,
        "frontend/index.html",
        {},
    )


def tutor_page(request):
    return render(
        request,
        "frontend/tutor.html",
        {},
    )
