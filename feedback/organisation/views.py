from .models import Gymkhana_body
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from polls.models import Question, Choice
from feedback.forms import QuestionForm
from django.utils import timezone


def index(request):
    body_list = Gymkhana_body.objects.all()
    return render(request, 'organisation/index.html', {'body_list': body_list})


def get_question(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = QuestionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            new_question = Question()
            new_question.body = Gymkhana_body.objects.get(
                nameofbody=form.cleaned_data['body'])
            new_question.question_text = form.cleaned_data['question']
            new_question.pub_date = timezone.now()
            new_question.save()

            choice1 = Choice()
            choice1.question = new_question
            choice1.choice_text = form.cleaned_data['choice1']
            choice1.votes = 0
            choice1.save()

            if form.cleaned_data['choice2']:
                choice2 = Choice()
                choice2.question = new_question
                choice2.choice_text = form.cleaned_data['choice2']
                choice2.votes = 0
                choice2.save()

            if form.cleaned_data['choice3']:
                choice3 = Choice()
                choice3.question = new_question
                choice3.choice_text = form.cleaned_data['choice3']
                choice3.votes = 0
                choice3.save()

            if form.cleaned_data['choice4']:
                choice4 = Choice()
                choice4.question = new_question
                choice4.choice_text = form.cleaned_data['choice4']
                choice4.votes = 0
                choice4.save()

            # redirect to a new URL:
            messages.add_message(request, messages.SUCCESS,
                                 'Thanks for your suggestion!')
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = QuestionForm()

    return render(request, 'organisation/addquestion.html', {'form': form})
