from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.Login, name="login"),
    path("logout/", views.Logout, name="logout"),
    path("home/", views.home, name="home"),
    path("home/<int:id_student>", views.detail_student, name="detail_student"),
    path("add-student/", views.get_name, name="add_student"),
    path("search-student/", views.search_student, name="search_student"), 
    path("delete-student/<int:id_student>", views.delete_student, name="delete_student"),
    path("update-student/<int:id_student>", views.update_student, name="update_student"),

    path("your-name/", views.get_name, name="get_name"), 

    path("submit", views.submit, name="submit"),

    path("str/<int:my_char>", views.char, name="char"),
    # path("str2/<int:my_char>", views.char2, name="char2"),

    # ex: /polls/5/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]