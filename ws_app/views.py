from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'ws_app/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'ws_app/detail.html', {'question': question})


def results(request, question_id):
    return HttpResponse(f"You're looking at results of thing {question_id}")


def vote(request, question_id):
    return HttpResponse(f"You're voting on thing {question_id}")
