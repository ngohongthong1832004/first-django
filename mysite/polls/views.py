from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import Http404
from .models import Question
from django.template import loader
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .forms import *

from .models import Choice, Question, TestImport, ListStudent

def Login(request):

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(username=username, password=password)
            if user is not None:
                # A backend authenticated the credentials
                print("A backend authenticated the credentials")
                print("user name : ", user.get_full_name())
                username = user.get_full_name()
                login(request, user)
                return HttpResponseRedirect("/home",{"user",username})
                # login(request, user)
            else:
                # No backend authenticated the credentials
                print("No backend authenticated the credentials")
    else:
        form = LoginForm()

    return render(request, "polls/login.html", {"form": form})

def Logout (request):
    logout(request)
    return HttpResponseRedirect("/login")

@login_required(login_url="/login")
def home(request):
    list_student = ListStudent.objects.all()
    print("list_student : ", list_student)
    return render(request, "polls/home.html", {"list_student": list_student})
@login_required(login_url="/login")
def detail_student(request, id_student):
    student = ListStudent.objects.get(pk=id_student)
    # print("student : ", student.first_name)
    return render(request, "polls/detail_student.html", {"student": student})
@login_required(login_url="/login")
def delete_student(request, id_student):
    student = ListStudent.objects.get(pk=id_student)
    student.delete()
    # print("student : ", student.first_name)
    return HttpResponseRedirect("/home")
@login_required(login_url="/login")
def update_student(request, id_student):
    student = ListStudent.objects.get(pk=id_student)
    if request.method == "POST":
        form = UpdateForm(request.POST)
        if form.is_valid():
            student.first_name = form.cleaned_data["first_name"]
            student.last_name = form.cleaned_data["last_name"]
            student.age = form.cleaned_data["age"]
            student.save()
            return HttpResponseRedirect("/home")
    else:
        form = UpdateForm(initial={"first_name": student.first_name, "last_name": student.last_name, "age": student.age})
    # print("student : ", student.first_name)
    return render(request, "polls/update_student.html", {"form": form})

@login_required(login_url="/login")
def char(request, my_char):
    print("my_char : ", my_char)
    return HttpResponse(my_char)

class char2(generic.DetailView):
    def __str__(self, **kwargs):
        testel = kwargs.get("my_char")
        print("testel : ", testel)
        return kwargs.my_char

@login_required(login_url="/login")
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # print("latest_question_list : ", latest_question_list)
    context = {"latest_question_list": latest_question_list}
    # print("context : ", context)
    return render(request, "polls/index.html", context)

@login_required(login_url="/login")
def test(request):
    templateHTML = loader.get_template("polls/add_student.html")
    return HttpResponse(templateHTML.render())
@login_required(login_url="/login")
def submit (request):
    return HttpResponse("Submit : ")
@login_required(login_url="/login")
def layout(request):
    return render(request, "polls/search_student.html")

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

@login_required(login_url="/login")
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})
@login_required(login_url="/login")
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

@login_required(login_url="/login")
def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            first_name = form.cleaned_data["your_name"]
            last_name = form.cleaned_data["bio"]
            your_age = form.cleaned_data["your_age"]
            # ...
            # redirect to a new URL:
            add_new_user = ListStudent.objects.create(first_name=first_name, last_name=last_name, age=your_age)
            add_new_user.save()
            return HttpResponseRedirect("/home/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, "polls/add_student.html", {"form": form})
@login_required(login_url="/login")
def search_student(request):
    if request.method =="POST" :
        form = SearchForm(request.POST)

        if form.is_valid():
            search_text = form.cleaned_data["search_name"]

            list_student = ListStudent.objects.filter(last_name__contains=search_text)
            return render(request, "polls/search_student.html", {"list_student" : list_student, "form" : form, "search_text" : search_text })
    else:
        form = SearchForm()
        # print("form-else : ", form)


    return render(request, "polls/search_student.html", {"form" : form })


    
