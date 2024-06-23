from django.db.models import F
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse

from hangul_tutor.hangul_tutor_app.models import Choice
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
    question = get_object_or_404(Question, pk=question_id)
    return render(
        request,
        "hangul_tutor_app/results.html",
        {
            "question": question,
        },
    )


def vote(
    request: HttpRequest,
    question_id: int,
) -> HttpResponse:
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])  # type: ignore
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(
            reverse(
                "hangul_tutor_app:results",
                args=(question.id,),  # type: ignore
            )
        )
