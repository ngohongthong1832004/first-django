from django.shortcuts import render
from django.http import Http404
from .models import Question
from django.urls import reverse
from django.template import loader
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Choice, Question, TestImport, ListStudent

def home(request):
    list_student = ListStudent.objects.all()
    print("list_student : ", list_student)
    return render(request, "polls/home.html", {"list_student": list_student})


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # print("latest_question_list : ", latest_question_list)
    context = {"latest_question_list": latest_question_list}
    # print("context : ", context)
    return render(request, "polls/index.html", context)


def test(request):
    templateHTML = loader.get_template("polls/add_student.html")
    return HttpResponse(templateHTML.render())



def layout(request):
    return render(request, "polls/search_student.html")

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
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
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))