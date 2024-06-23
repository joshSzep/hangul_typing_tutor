from django.http import Http404
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render

from hangul_tutor.hangul_tutor_app.models import Question


def index(
    request: HttpRequest,
) -> HttpResponse:
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(
        request,
        "hangul_tutor_app/index.html",
        context,
    )


def detail(
    request: HttpRequest,
    question_id: int,
) -> HttpResponse:
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(
        request,
        "hangul_tutor_app/detail.html",
        {"question": question},
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
