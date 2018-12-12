from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.db.models import F
import logging

from django.views import generic

from organisation.models import Gymkhana_body
from .models import Question, Choice


def index(request, body_id):
    body = get_object_or_404(Gymkhana_body, pk=body_id)
    latest_question_list = body.question_set.all()
    context = {'latest_question_list': latest_question_list, 'body': body}
    return render(request, 'polls/index.html', context)


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    body = question.body
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/index.html', {
            'body': body,
            'latest_question_list': body.question_set.all(),
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes = F('votes')+1
        selected_choice.save()
        question.totalvotes = F('totalvotes')+1
        question.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:index', args=(body.id,)))


def combinedresult(request, body_id):
    body = get_object_or_404(Gymkhana_body, pk=body_id)
    latest_question_list = body.question_set.all()
    context = {'latest_question_list': latest_question_list, 'body': body}
    return render(request, 'polls/combinedresults.html', context)
