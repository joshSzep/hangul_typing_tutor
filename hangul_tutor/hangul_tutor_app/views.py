from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from hangul_tutor.hangul_tutor_app.models import Question


def index(
    request: HttpRequest,
) -> HttpResponse:
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    return render(
        request,
        "hangul_tutor_app/index.html",
        {
            "latest_question_list": latest_question_list,
        },
    )


def detail(
    request: HttpRequest,
    question_id: int,
) -> HttpResponse:
    question = get_object_or_404(Question, pk=question_id)
    return render(
        request,
        "hangul_tutor_app/detail.html",
        {
            "question": question,
        },
    )


def results(
    request: HttpRequest,
    question_id: int,
) -> HttpResponse:
    return HttpResponse(f"You're looking at the results of question {question_id}.")


def vote(
    request: HttpRequest,
    question_id: int,
) -> HttpResponse:
    return HttpResponse(f"You're voting on question {question_id}.")
