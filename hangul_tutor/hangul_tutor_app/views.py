from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the hangul_tutor_app index.")


def detail(
    request,
    question_id: int,
):
    return HttpResponse(f"You're looking at question {question_id}.")


def results(
    request,
    question_id: int,
):
    return HttpResponse(f"You're looking at the results of question {question_id}.")


def vote(
    request,
    question_id: int,
):
    return HttpResponse(f"You're voting on question {question_id}.")
