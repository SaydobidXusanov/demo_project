from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader

from polls.models import Question


# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    selected_question = Question.objects.get(pk=int(question_id))
    question_choices = selected_question.choice_set.all()
    context = {
        "question": selected_question,
        "question_choices_list": question_choices,
    }

    template = loader.get_template("polls/question.html")
    return HttpResponse(template.render(context, request))


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id, choice_id):
    selected_question = Question.objects.get(pk=question_id)
    choice_to_vote = selected_question.choice_set.get(pk=choice_id)
    choice_to_vote.votes += 1
    choice_to_vote.save()
    return redirect('detail', question_id=question_id)
